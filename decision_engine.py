"""
decision_engine.py
Injini ya kuamua/ku-rank dawa kutokana na target za mgonjwa + toxicity data.

TAHADHARI KUBWA (soma kabla ya kutumia):
- IC50 ya in-vitro (maabara) SIYO uthibitisho wa ufanisi kwa binadamu (in-vivo).
- API.py ya awali ilivuta EFFICACY (IC50/EC50) tu - HAIKUWA na toxicity data.
  Function ya fetch_toxicity_data() hapa chini inaziba pengo hilo kwa
  kuvuta assay za CC50/TC50 (cytotoxicity dhidi ya seli za binadamu).
- Matokeo ya function hizi ni PENDEKEZO la awali la utafiti, SIYO agizo la
  matibabu. Uamuzi wa mwisho lazima ufanywe na mtaalamu wa afya aliyesajiliwa.
"""

import pandas as pd
from chembl_webresource_client.new_client import new_client


def fetch_toxicity_data(target_chembl_ids=None, limit=2000):
    """
    Vuta assay za cytotoxicity (CC50/TC50) dhidi ya seli za binadamu, kama
    kiashiria cha awali cha 'madhara yanayowezekana'. Hii ni NYONGEZA muhimu
    kwa API.py ya awali (ambayo ilivuta efficacy pekee).
    """
    activity = new_client.activity
    query = activity.filter(standard_type__in=["CC50", "TC50"], relation="=")

    rows = []
    for item in query[:limit]:
        smiles = item.get("canonical_smiles")
        val = item.get("standard_value")
        assay_desc = item.get("assay_description") or ""
        if smiles and val:
            rows.append({
                "SMILES": smiles,
                "Toxicity_nM": float(val),
                "Assay_Info": assay_desc,
            })
    return pd.DataFrame(rows)


def rank_drug_candidates(efficacy_df, toxicity_df, target_chembl_ids,
                          patient_allergy_smiles=None):
    """
    efficacy_df : DataFrame kutoka API.py (full_dataset) - ina SMILES,
                  Target_ID, Value_nM, Is_Effective
    toxicity_df : DataFrame kutoka fetch_toxicity_data()
    target_chembl_ids : orodha ya targets zinazolingana na kile YOLO
                         ilichokigundua (kutoka mapping_engine)
    patient_allergy_smiles : orodha ya SMILES ambazo mgonjwa ana mzio nazo
                              (hiari - bado inahitaji chanzo cha data cha
                              mzio wa mgonjwa, ambacho hakipo bado)

    Returns: (DataFrame ya dawa zilizo-rank, status_message)
    """
    candidates = efficacy_df[
        efficacy_df["Target_ID"].isin(target_chembl_ids)
        & (efficacy_df["Is_Effective"] == 1)
    ].copy()

    if candidates.empty:
        return pd.DataFrame(), (
            "Hakuna dawa zenye ushahidi wa ufanisi (IC50) dhidi ya target "
            "hizi kwenye dataset."
        )

    merged = candidates.merge(toxicity_df, on="SMILES", how="left")

    # Selectivity Index: Toxicity_nM (kubwa) / Efficacy_nM (ndogo) = kubwa
    # zaidi -> dawa ina nguvu dhidi ya kimelea LAKINI si sumu kwa seli za
    # binadamu (salama zaidi).
    merged["Selectivity_Index"] = merged["Toxicity_nM"] / merged["Value_nM"]

    if patient_allergy_smiles:
        merged["is_allergy_risk"] = merged["SMILES"].isin(patient_allergy_smiles)
    else:
        merged["is_allergy_risk"] = False

    def classify(row):
        if row["is_allergy_risk"]:
            return "MADHARA - Epuka (mzio wa mgonjwa)"
        if pd.isna(row["Selectivity_Index"]):
            return "Efficacy ipo, toxicity haijulikani - tahadhari, chunguza zaidi"
        if row["Selectivity_Index"] >= 10:
            return "Inapendekezwa - Bora"
        if row["Selectivity_Index"] >= 2:
            return "Inafaa - Mzuri wa kati"
        return "MADHARA - Selectivity Index ndogo (hatari ya sumu)"

    merged["recommendation"] = merged.apply(classify, axis=1)

    merged = merged.sort_values(
        by=["is_allergy_risk", "Selectivity_Index"], ascending=[True, False]
    )

    cols = ["SMILES", "Target_ID", "Value_nM", "Toxicity_nM",
            "Selectivity_Index", "recommendation"]
    return merged[cols], "OK"
