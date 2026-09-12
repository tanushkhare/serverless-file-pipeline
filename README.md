# ⚡ Serverless File Pipeline

[![Live Web Demo](https://img.shields.io/badge/Live_App-Vercel-black?style=for-the-badge&logo=vercel)](https://serverless-file-pipeline.vercel.app)
[![Portfolio Hub](https://img.shields.io/badge/Portfolio_Hub-Live-blue?style=for-the-badge)](https://portfolio-showcase-hub-web11.vercel.app)

🔗 **Production URL:** [https://serverless-file-pipeline.vercel.app](https://serverless-file-pipeline.vercel.app)  
🌐 **Showcase Hub:** [https://portfolio-showcase-hub-web11.vercel.app](https://portfolio-showcase-hub-web11.vercel.app)

---

## 📌 Architectural Overview
Event-driven file processing pipeline with dead-letter queue (DLQ) retry policies and schema validation.

---

## 🛠️ Technology Ecosystem
* **Core Architecture:** FastAPI, MinIO / S3, Docker, AsyncIO
* **Testing & Quality:** PyTest, Automated GitHub Actions CI
* **Deployment:** Vercel Edge Runtime

---

## 🚀 API Contracts
```http
POST /api/v1/pipeline/process
GET /health
```

---

## 💻 Local Quickstart
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
pytest tests/ -v
```
