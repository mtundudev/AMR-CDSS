"""
mapping_engine.py
Daraja kati ya class za YOLO (AMR.ipynb) na targets za ChEMBL/PubChem (API.py)

MUHIMU - SOMA KABLA YA KUTUMIA:
Hii ni prototype ya utafiti/maendeleo (R&D). SIYO kifaa cha uchunguzi wa
kimatibabu kilichoidhinishwa. Usitumike kutibu mgonjwa halisi bila:
  1) Uthibitisho wa kikliniki (validation dhidi ya ground truth halisi)
  2) Ukaguzi wa daktari/pharmacologist aliyesajiliwa
  3) Kibali cha mamlaka husika za afya (mf. TMDA - Tanzania, FDA, EMA)
  4) Utaratibu wa "human-in-the-loop" - pendekezo la mfumo SIYO uamuzi wa
     mwisho wa matibabu
"""

from chembl_webresource_client.new_client import new_client

# Ramani ya awali: class ya YOLO (kutoka data.yaml) -> jina la kisayansi la
# kiumbe. ONGEZA/REKEBISHA orodha hii kulingana na class_names HALISI za
# data.yaml yako baada ya training.
CLASS_TO_ORGANISM = {
    # -------- Malaria (kutoka AMR.ipynb / BCCD dataset) --------
    "Ring": "Plasmodium falciparum",
    "Trophozoite": "Plasmodium falciparum",
    "Schizont": "Plasmodium falciparum",
    "Gametocyte": "Plasmodium falciparum",

    # -------- Bakteria (AMR halisi) --------
    # HAYA NI MIFANO TU. Badilisha kulingana na class_names za dataset yako
    # halisi ya 'bacteria detection.v3i.yolov8' (angalia data.yaml).
    "Gram_positive_cocci": "Staphylococcus aureus",
    "Gram_negative_rod": "Escherichia coli",
    "Mycobacterium": "Mycobacterium tuberculosis",
}

# Cache ili tusipige query ChEMBL mara kwa mara kwa organism ile ile
_target_cache = {}


def get_targets_for_organism(organism_name, limit=20):
    """
    Tafuta target_chembl_id zote zinazohusiana na kiumbe fulani (organism),
    kwa kutumia jina la kisayansi moja kwa moja dhidi ya ChEMBL API - badala
    ya kutumia ID zilizowekwa fixed (hardcoded), kwa sababu ID fixed bila
    uthibitisho wa moja kwa moja ni hatari ya kutoa taarifa isiyo sahihi.
    """
    if organism_name in _target_cache:
        return _target_cache[organism_name]

    target = new_client.target
    results = target.filter(organism__icontains=organism_name).only(
        ["target_chembl_id", "pref_name", "target_type", "organism"]
    )[:limit]

    targets = list(results)
    _target_cache[organism_name] = targets
    return targets


def resolve_targets_for_class(yolo_class_name):
    """
    Kutoka class iliyogunduliwa na YOLO -> orodha ya target_chembl_id husika.
    """
    organism = CLASS_TO_ORGANISM.get(yolo_class_name)
    if organism is None:
        return {
            "error": (
                f"Class '{yolo_class_name}' haipo kwenye CLASS_TO_ORGANISM. "
                f"Ongeza kwenye mapping kabla ya kuendelea."
            )
        }

    targets = get_targets_for_organism(organism)
    return {
        "yolo_class": yolo_class_name,
        "organism": organism,
        "target_chembl_ids": [t["target_chembl_id"] for t in targets],
        "target_details": targets,
    }
