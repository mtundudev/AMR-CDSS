# AMR-CDSS
AMR CDSS: AI-Powered Antimicrobial Resistance Clinical Decision Support System

# Clinical-Decision-Support-System
AI-powered microscopic image analysis and clinical decision support using YOLOv8, FastAPI, PostgreSQL, and edge computing.

# 🧬 Clinical AI — Clinical Decision Support System backend

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/YOLOv8-Computer%20Vision-111111?style=for-the-badge" alt="YOLOv8">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00A8FF&center=true&vCenter=true&width=850&lines=Detecting+Microscopic+Objects...;Counting+Blood+Components...;Applying+Clinical+Rules...;Validating+Treatment...;Alerting+on+Critical+Values...;Supporting+Clinical+Decisions..." alt="Typing Animation">
</p>

<p align="center">
  <strong>SEE → COUNT → CHECK → SUPPORT</strong>
</p>

<p align="center">
  An AI-powered Clinical Decision Support System that assists laboratory personnel and physicians in analyzing microscopic blood/pathogen samples, validating proposed treatments, and tracking patient results — deployable on cloud or offline edge hardware.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-early--development-orange?style=flat-square" alt="Status">
  &nbsp;
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=flat-square" alt="Build">
</p>

> ⚠️ **Status: Early Development (MVP stage).** Core architecture is defined; implementation is in progress. See [Roadmap](#-roadmap) for current completion state.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem & Solution](#-problem--solution)
- [Core Concept](#-core-concept)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [YOLOv8 Vision Engine](#-yolov8-vision-engine)
- [Clinical Decision Support](#-clinical-decision-support)
- [Medication Validation](#-medication-validation)
- [Patient & Sample Tracking](#-patient--sample-tracking)
- [Audit Trail & Access Control](#-audit-trail--access-control)
- [Alerts & Notifications](#-alerts--notifications)
- [Reporting & Export](#-reporting--export)
- [Offline-First & Edge Sync](#-offline-first--edge-sync)
- [Multi-language Support](#-multi-language-support)
- [Feedback Loop & Model Improvement](#-feedback-loop--model-improvement)
- [Edge Hardware](#-edge-hardware)
- [Backend Structure](#-backend-structure)
- [API Endpoints](#-api-endpoints)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Running the Backend](#-running-the-backend)
- [Testing](#-testing)
- [Docker](#-docker)
- [Security Considerations](#-security-considerations)
- [Roadmap](#-roadmap)
- [Clinical Safety](#-clinical-safety)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🔬 Overview

Clinical AI CDSS combines:

- 🔬 Microscopic imaging
- 🤖 YOLOv8 computer vision
- ⚡ FastAPI backend
- 🗄️ PostgreSQL database
- 🧠 Rule-based clinical decision support
- 💊 Medication validation
- 🧾 Patient/sample history tracking
- 🔔 Critical-value alerting (in-app + SMS)
- 🖥️ Frontend visualization
- ⚙️ Offline edge computing

> **Important:** This system is designed to *support* clinical decision-making — it does not replace qualified healthcare professionals.

---

## 🎯 Problem & Solution

Manual microscopic analysis is repetitive, time-consuming, and prone to human counting error. Clinical AI CDSS automates detection and counting, cross-references results against configured clinical rules, and validates proposed treatments — while keeping a full audit trail of every decision.

```
Microscopic Sample → Digital Camera → YOLOv8 Detection → Object Counting
        → Clinical Rule Evaluation → Analysis Result → Frontend Dashboard
        → Clinical Decision Support → Medication Validation → Patient Record
```

---

## 🧠 Core Concept

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   SEE    │ --> │  COUNT   │ --> │  CHECK   │ --> │ SUPPORT  │
│ YOLOv8   │     │ Aggregate│     │ Clinical │     │ Decision │
│ detects  │     │ counts   │     │  rules   │     │ + record │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

- **SEE** — the vision model detects objects in the microscopic image.
- **COUNT** — detections are aggregated into numerical totals.
- **CHECK** — the backend evaluates results against configured clinical rules.
- **SUPPORT** — structured, auditable information is presented to the clinician, linked to the patient record.

---

## 🏗️ System Architecture

```
Microscopic Slide → Digital Camera → YOLOv8 (best.pt)
                                         │
                          ┌──────────────┴──────────────┐
                          ▼                              ▼
                  Visual Detection               Object Counting
                  (Bounding Boxes)               (Quantitative Data)
                          │                              │
                          └──────────────┬───────────────┘
                                         ▼
                                     FastAPI
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
             PostgreSQL          Clinical Rule Engine   Notification Service
          (patients, samples,    (thresholds, warnings)   (SMS / in-app alerts)
           audit logs, roles)
                    │                    │                    │
                    └────────────────────┼────────────────────┘
                                         ▼
                                  Analysis Result
                                         │
                                         ▼
                              Frontend Dashboard
                                         │
                                         ▼
                            Proposed Medication
                                         │
                                         ▼
                     POST /api/v1/validate-medication
                                         │
                                         ▼
                             Treatment Rule Engine
                                    │       │
                              ┌─────┘       └─────┐
                              ▼                   ▼
                         APPROVED          WARNING / MISMATCH
                              │                   │
                              └─────────┬─────────┘
                                        ▼
                          Patient Record + Audit Log + PDF Report
```

---

## ✨ Key Features

### Core Analysis
- 🔬 **Microscopic Image Analysis** — analyze samples with a custom-trained YOLOv8 model.
- 🤖 **AI Object Detection** — detect configured blood components or microbial classes.
- 📊 **Quantitative Analysis** — convert detections into numerical counts.
- 🖼️ **Visual Annotations** — bounding boxes with class and confidence overlay.
- 🧠 **Clinical Rule Engine** — evaluate results against configured thresholds.
- 💊 **Medication Validation** — validate a proposed drug against the detected pathogen.

### Patient & Workflow Management
- 🧾 **Patient & Sample Tracking** — every analysis is linked to a patient/sample ID, enabling historical trend views (e.g., CBC over time).
- 🕵️ **Audit Trail** — every analysis, validation, and medication decision is logged with user, timestamp, and outcome.
- 🔐 **Role-Based Access Control** — distinct permissions for Lab Technician, Doctor, and Admin roles.
- ✅ **Image Quality Pre-Check** — flags blurry, over/under-exposed, or out-of-focus images before running inference.
- 📦 **Batch Analysis** — process multiple samples in a single session.

### Alerts & Communication
- 🔔 **Critical Value Alerts** — automatic flag when a result crosses a dangerous threshold (e.g., abnormally high WBC).
- 📲 **SMS Notifications** — optional SMS alert to the attending physician for urgent results (via Africa's Talking or similar gateway), useful in low-connectivity settings.
- 📧 **In-App & Email Notifications** — configurable notification channels.

### Reporting & Data
- 📄 **PDF Report Export** — generate a printable/shareable report per analysis for the patient file.
- 🔄 **Offline-First Sync** — edge devices queue results locally and sync to the central server/HIMS when connectivity returns.
- 🌍 **Multi-language UI** — Kiswahili and English interface support.

### AI & Continuous Improvement
- ✏️ **Clinician Feedback Loop** — doctors can correct mislabeled detections; corrections are stored for future model retraining.
- ⚡ **REST API** — full analysis and validation workflow exposed via FastAPI.
- 🗄️ **Persistent Database** — stores rules, pathogens, medications, treatment mappings, patients, samples, and audit logs.
- 📴 **Edge Computing** — deployable on local hardware for offline environments.

---

## 🤖 YOLOv8 Vision Engine

```json
{
  "detections": [
    { "class": "RBC", "confidence": 0.94, "bbox": [120, 80, 180, 140] },
    { "class": "E_coli", "confidence": 0.87, "bbox": [200, 140, 240, 180] }
  ],
  "image_quality": { "blur_score": 0.12, "status": "acceptable" }
}
```

> Confidence reflects the model's detection confidence — **not** medical or diagnostic certainty.

---

## 🧠 Clinical Decision Support

```
AI Observation → Quantitative Results → Clinical Rules → Decision Support
      → Patient Record → Healthcare Professional
```

The clinician remains responsible for the final interpretation, alongside confirmatory procedures.

---

## 💊 Medication Validation

**Endpoint:** `POST /api/v1/validate-medication`

```
Detected Pathogen + Proposed Medication → Treatment Rules → Validation
        → APPROVED  |  WARNING / MISMATCH  →  Suggested confirmatory tests
```

> The system never invents clinical guidance — treatment rules must be sourced from validated, authoritative references.

---

## 🧾 Patient & Sample Tracking

- Every sample is linked to a `patient_id` and `sample_id`.
- Analysis history per patient is retrievable for trend monitoring (e.g., repeated CBC results).
- Sample metadata: collection date, technician, device/edge-node ID, image reference.

```
Patient ──< Sample ──< Analysis ──< MedicationValidation
```

---

## 🕵️ Audit Trail & Access Control

| Role            | Upload Sample | Run Analysis | Propose Medication | Validate Medication | View Audit Log |
|-----------------|:---:|:---:|:---:|:---:|:---:|
| Lab Technician  | ✅ | ✅ | ❌ | ❌ | ❌ |
| Doctor          | ❌ | ✅ | ✅ | ✅ | ❌ |
| Admin           | ✅ | ✅ | ✅ | ✅ | ✅ |

Every state-changing action is recorded: **who, what, when, and result** — required for clinical accountability, even at prototype stage.

---

## 🔔 Alerts & Notifications

```
Analysis Result → Threshold Breach? ── yes ──> In-App Alert + SMS to Doctor
                          │
                          no
                          ▼
                    Standard Result
```

SMS delivery is designed around low-connectivity environments common in rural laboratory settings.

---

## 📄 Reporting & Export

- Generate a per-analysis **PDF report** (annotated image, counts, rule findings, medication validation outcome).
- Reports are stored and linked to the patient/sample record for future retrieval.

---

## 🔄 Offline-First & Edge Sync

```
Edge Node (offline) → Local Queue (SQLite/local Postgres)
        → Connectivity Restored → Sync Worker → Central Server / HIMS
```

Edge nodes continue operating fully offline; sync is eventually-consistent once network access resumes.

---

## 🌍 Multi-language Support

UI strings are externalized for translation — **Kiswahili** and **English** supported out of the box, extensible to other languages.

---

## ✏️ Feedback Loop & Model Improvement

```
Clinician flags incorrect detection → Correction stored → Dataset growth
        → Periodic retraining → Updated best.pt → Redeploy
```

---

## ⚙️ Edge Hardware


Digital Microscope Camera (C-Mount)
            │  (USB / CSI video stream)
            ▼
Edge Processing Unit: Nvidia Jetson Nano (preferred, CUDA) / Raspberry Pi 4 (fallback, ONNX/TFLite)
            │  (Offline FastAPI + YOLOv8 inference)
            ▼
Touchscreen Interface Panel (Frontend UI)
```
backend/
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
├── models/
│   ├── patient.py
│   ├── sample.py
│   ├── clinical_rule.py
│   ├── pathogen.py
│   ├── medication.py
│   ├── treatment_rule.py
│   ├── analysis.py
│   └── audit_log.py
├── schemas/
│   ├── patient.py
│   ├── analysis.py
│   └── medication.py
├── services/
│   ├── yolo_service.py
│   ├── analysis_service.py
│   ├── clinical_rule_service.py
│   ├── medication_service.py
│   ├── notification_service.py
│   ├── report_service.py
│   └── sync_service.py
├── routers/
│   ├── analysis.py
│   ├── medication.py
│   ├── patients.py
│   └── reports.py
└── main.py
```

---

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `POST` | `/api/v1/analyze` | Upload a microscopic image and run AI analysis |
| `POST` | `/api/v1/validate-medication` | Validate proposed medication against detected pathogen |
| `GET`  | `/api/v1/patients/{id}/history` | Retrieve a patient's analysis history |
| `GET`  | `/api/v1/reports/{analysis_id}` | Generate/download a PDF report for an analysis |
| `GET`  | `/api/v1/audit-logs` | Retrieve audit trail (Admin only) |
| `POST` | `/api/v1/analysis/{id}/feedback` | Submit a correction on a detection |

---

## 🚀 Installation

```bash
git clone https://github.com/mtundudev/clinical-ai-cdss.git
cd clinical-ai-cdss

python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/clinical_ai` |
| `SECRET_KEY` | JWT/auth signing secret | `change-me` |
| `MODEL_PATH` | Path to trained YOLOv8 weights | `./models/best.pt` |
| `SMS_API_KEY` | SMS gateway API key (e.g. Africa's Talking) | `your-api-key` |
| `DEFAULT_LANGUAGE` | Default UI language | `sw` or `en` |

> Never commit `.env` or production secrets to GitHub.

## 🗃️ Database Setup

```bash
alembic upgrade head
```

## ▶️ Running the Backend

```bash
uvicorn backend.main:app --reload
```

Interactive docs: `/docs` and `/redoc`

## 🧪 Testing

```
tests/
├── test_analysis.py
├── test_yolo_service.py
├── test_clinical_rules.py
├── test_medication.py
├── test_patients.py
├── test_audit_log.py
└── test_api.py
```

```bash
pytest
```

## 🐳 Docker

```
Docker Host
 ├── FastAPI Application
 ├── PostgreSQL
 └── Notification/Sync Worker
```

---

## 🔐 Security Considerations

- Environment-based secrets management
- JWT authentication + role-based authorization
- Input & file-upload validation
- Safe model loading
- Full audit logging of clinical actions
- Patient-data privacy — access restricted by role, data encrypted at rest where applicable
- Compliance alignment target: relevant national health-data protection requirements (to confirm with local regulatory guidance before any clinical use)

---

## 🛣️ Roadmap

**Phase 1 — Foundation**
- [x] Define system architecture
- [ ] Backend structure, PostgreSQL, SQLAlchemy, Alembic setup

**Phase 2 — AI Integration**
- [ ] Integrate `best.pt`, inference, detection extraction, counting

**Phase 3 — Analysis API**
- [ ] `/api/v1/analyze`, image validation, rule integration, response schemas

**Phase 4 — Clinical Decision Support**
- [ ] Rule models, evaluation service, warning generation, analysis history

**Phase 5 — Medication Validation**
- [ ] Medication models, treatment rules, `/api/v1/validate-medication`

**Phase 6 — Patient, Audit & Alerts**
- [ ] Patient/Sample models, audit log, RBAC, critical-value alerts, SMS integration

**Phase 7 — Reporting & Sync**
- [ ] PDF report generation, offline queue, edge-to-server sync

**Phase 8 — Frontend**
- [ ] Image upload, live feed, annotated display, dashboard, clinical action panel, Kiswahili/English toggle

**Phase 9 — Edge Deployment**
- [ ] Camera integration, Jetson Nano/Pi 4 testing, inference benchmarking, offline deployment

**Phase 10 — Integration & Validation**
- [ ] HIMS integration research, security review, clinical validation planning

---

## ⚠️ Clinical Safety

This project is a **Clinical Decision Support System prototype** — not an autonomous diagnostic or prescribing system. AI detections and rule-based outputs may contain errors. Final clinical decisions remain the responsibility of qualified healthcare professionals, following applicable clinical guidelines, laboratory procedures, and regulations. Clinical thresholds and treatment rules must come from authoritative, validated sources — never invented or assumed by the system.

---

## 🤝 Contributing

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request. Fork the repo, create a feature branch, and submit a PR with a clear description of the change and its clinical/technical rationale.

---

## 👤 Author

**Dotto Mtundu Hamis (Mtundu)**
Backend Developer (FastAPI / Python) — Mbeya, Tanzania
GitHub: [@mtundudev](https://github.com/mtundudev)

---

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
