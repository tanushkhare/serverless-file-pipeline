# ⚡ Serverless File Pipeline

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://serverless-file-pipeline.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://serverless-file-pipeline.vercel.app](https://serverless-file-pipeline.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Event-driven simulated S3 object ingestion pipeline processing file notifications with dead-letter queue (DLQ) retry policies and schema validation.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, MinIO / S3, Docker, AsyncIO
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🛡️ Production Standards
* **Router Mounted:** Fully connected `pipeline_router` on `/api/v1/pipeline`.
* **DLQ Retries:** Quarantines corrupt uploads and performs exponential backoff attempts.
* **Latency Emission:** Emits execution time and throughput telemetry.

---

## 🚀 API Contracts
```http
POST /api/v1/pipeline/process
Request:
{
  "file_name": "financial_telemetry_2026.parquet",
  "size_kb": 4850
}

Response (200 OK):
{
  "status": "PROCESSED",
  "metadata": {"format": "parquet", "records": 8200},
  "latency_ms": 22.4,
  "dlq_status": "NONE"
}

GET /health
Response: {"status": "healthy"}

💻 Local Quickstart

Bash

pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v