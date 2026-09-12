import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_process_s3_file_event():
    payload = {
        "bucket_name": "test-data-bucket",
        "object_key": "raw/logs/test_file.pdf",
        "file_size_kb": 250.0,
        "mime_type": "application/pdf"
    }
    res = client.post("/api/v1/pipeline/process-event", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "EVT-" in data["event_id"]
    assert data["status"] == "PROCESSED_SUCCESSFULLY"
    assert data["total_execution_ms"] > 0
    assert "stage_latencies_ms" in data
