import streamlit as st
import requests

st.set_page_config(page_title="Serverless File Pipeline", layout="wide")

st.title("⚡ Event-Driven Serverless File Ingestion Pipeline")
st.markdown("Automated S3 object creation triggers, asynchronous lambda execution stages, and structured metadata transformation.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Simulate S3 Bucket Upload Trigger")
    bucket = st.text_input("Source S3 Bucket", value="enterprise-raw-ingestion")
    key = st.text_input("Object Key / Path", value="financial_reports/2026_q3_report.pdf")
    mime = st.selectbox("MIME Type", ["application/pdf", "text/csv", "application/json", "image/png"])
    size = st.slider("File Size (KB)", 10.0, 5000.0, 350.0)

    if st.button("Dispatch S3 Event Notification", type="primary"):
        with st.spinner("Processing event-driven transformation pipeline..."):
            try:
                res = requests.post(
                    "http://localhost:8000/api/v1/pipeline/process-event",
                    json={"bucket_name": bucket, "object_key": key, "file_size_kb": size, "mime_type": mime},
                    timeout=5
                )
                if res.status_code == 200:
                    st.session_state["p17_result"] = res.json()
                    st.success("File Processed by Serverless Worker!")
                else:
                    st.error(f"Pipeline Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Running client-side simulated pipeline run.")
                st.session_state["p17_result"] = {
                    "event_id": "EVT-SIM339",
                    "bucket": bucket,
                    "key": key,
                    "status": "PROCESSED_SUCCESSFULLY",
                    "stage_latencies_ms": {"s3_event_auth": 11.2, "payload_transformation": 22.4, "downstream_sink_delivery": 10.8},
                    "total_execution_ms": 44.4,
                    "output_destination": f"s3://{bucket}-processed/{key}.parquet",
                    "timestamp": "2026-08-28T08:15:00Z"
                }

with col2:
    if "p17_result" in st.session_state:
        res = st.session_state["p17_result"]
        st.subheader(f"Execution Telemetry: {res['event_id']}")
        
        m1, m2 = st.columns(2)
        m1.metric("Execution Latency", f"{res['total_execution_ms']} ms")
        m2.metric("Pipeline Status", "SUCCESS", delta="Worker Healthy")
        
        st.markdown(f"**Destination Object:** `{res['output_destination']}`")
        
        st.markdown("#### Stage Latency Breakdown (ms)")
        for stage, lat in res["stage_latencies_ms"].items():
            st.info(f"• **{stage.replace('_', ' ').title()}**: `{lat} ms`")
