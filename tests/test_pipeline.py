import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_s3_file_event_pipeline():
    payload = {
        "bucket_name": "raw-data-bucket",
        "object_key": "invoices/inv_9981.pdf",
        "file_size_kb": 250.0,
        "mime_type": "application/pdf"
    }
    res = client.post("/api/v1/pipeline/process-event", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "EVT-" in data["event_id"]
    assert data["status"] == "PROCESSED_SUCCESSFULLY"
    assert "parquet" in data["output_destination"]
