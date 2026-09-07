"""
pipeline.py
Mfumo kamili: Picha ya mgonjwa -> YOLO (AMR.ipynb) -> Mapping -> Ranking ya dawa

MATUMIZI (baada ya kutrain model kwenye AMR.ipynb na kuwa na best.pt, na
kuendesha API.py kupata offline_drug_training_data.csv):

    python pipeline.py --image picha_ya_mgonjwa.jpg --model best.pt \
        --efficacy_csv offline_drug_training_data.csv

TAHADHARI: Hii ni prototype ya utafiti. Angalia maelezo ya kimaadili/kliniki
kwenye mapping_engine.py na decision_engine.py kabla ya kutumia matokeo haya
kwa uamuzi wowote wa kweli wa matibabu. Matokeo ni PENDEKEZO la awali tu -
lazima yapitiwe na mtaalamu wa afya aliyesajiliwa.
"""

import argparse
import pandas as pd
from ultralytics import YOLO

from mapping_engine import resolve_targets_for_class
from decision_engine import fetch_toxicity_data, rank_drug_candidates


def detect_classes(image_path, model_path, conf_threshold=0.5):
    model = YOLO(model_path)
    results = model.predict(source=image_path, conf=conf_threshold)

    detected_classes = set()
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            detected_classes.add(cls_name)
    return list(detected_classes)


def run_pipeline(image_path, model_path, efficacy_csv, patient_allergy_smiles=None):
    print(f"[1/4] Inasoma picha: {image_path}")
    detected = detect_classes(image_path, model_path)
    print(f"      Vimegunduliwa: {detected}")

    if not detected:
        print("      Hakuna kitu kilichogundulika kwenye picha hii.")
        return None

    print("[2/4] Inatafuta targets za ChEMBL kwa kila kilichogundulika...")
    all_target_ids = set()
    for cls in detected:
        result = resolve_targets_for_class(cls)
        if "error" in result:
            print(f"      TAHADHARI: {result['error']}")
            continue
        all_target_ids.update(result["target_chembl_ids"])
    print(f"      Targets: {sorted(all_target_ids)}")

    if not all_target_ids:
        print("      Hakuna target zilizopatikana - haiwezekani kuendelea.")
        return None

    print("[3/4] Inapakia efficacy data (kutoka API.py) na toxicity data...")
    efficacy_df = pd.read_csv(efficacy_csv)
    toxicity_df = fetch_toxicity_data(target_chembl_ids=list(all_target_ids))

    print("[4/4] Inapanga (ranking) dawa...")
    ranked, status = rank_drug_candidates(
        efficacy_df, toxicity_df, list(all_target_ids),
        patient_allergy_smiles=patient_allergy_smiles,
    )

    if status != "OK":
        print(status)
        return None

    print("\n--- MATOKEO (Pendekezo la awali - SIYO agizo la matibabu) ---")
    print(ranked.to_string(index=False))
    return ranked


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--model", required=True, help="Njia ya best.pt")
    parser.add_argument("--efficacy_csv", default="offline_drug_training_data.csv")
    args = parser.parse_args()

    run_pipeline(args.image, args.model, args.efficacy_csv)
