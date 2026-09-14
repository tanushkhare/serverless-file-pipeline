import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #090d16;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        .sidebar .stSidebar {
            background-color: #0f172a;
            border-right: 1px solid #1e293b;
        }
        h1, h2, h3 {
            color: #f8fafc;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        .stButton>button {
            background: linear-gradient(135deg, #38bdf8 0%, #0284c7 100%);
            color: #090d16;
            font-weight: 600;
            border: none;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Serverless File Pipeline", layout="wide")

st.title("⚡ Serverless Event-Driven File Processing Pipeline")
st.markdown("Automated S3/LocalStack notification handling, async micro-stage execution, and columnar metadata routing.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Simulate S3 File Upload Event")
    bucket = st.text_input("Target S3 Ingest Bucket", value="enterprise-telemetry-raw-drop")
    key = st.text_input("Object Key / Storage Path", value="inbound/2026/08/payload_batch_441.pdf")
    size_kb = st.number_input("File Size (KB)", value=412.8, step=50.0)
    mime = st.selectbox("Content MIME Type", ["application/pdf", "text/csv", "application/json", "application/parquet"])

    if st.button("Dispatch S3 Event Notification", type="primary"):
        with st.spinner("Invoking serverless transformation pipeline..."):
            payload = {
                "bucket_name": bucket,
                "object_key": key,
                "file_size_kb": size_kb,
                "mime_type": mime
            }
            try:
                res = requests.post("http://localhost:8000/api/v1/pipeline/process-event", json=payload, timeout=5)
                if res.status_code == 200:
                    st.session_state["p17_result"] = res.json()
                    st.success("Event Processed Successfully!")
                else:
                    st.error(f"Pipeline Error: {res.text}")
            except Exception:
                st.warning("Backend offline. Simulating pipeline latency stages.")
                st.session_state["p17_result"] = {
                    "event_id": "EVT-SIM9921",
                    "bucket": bucket,
                    "key": key,
                    "status": "PROCESSED_SUCCESSFULLY",
                    "stage_latencies_ms": {
                        "auth_and_validation": 10.4,
                        "extraction_and_decompression": 21.2,
                        "metadata_and_routing": 11.5
                    },
                    "total_execution_ms": 43.1,
                    "output_destination": f"s3://{bucket}-processed/{key}.parquet",
                    "timestamp": "2026-08-28T11:15:00Z"
                }

with col2:
    if "p17_result" in st.session_state:
        r = st.session_state["p17_result"]
        st.subheader(f"Execution Event: {r['event_id']}")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Pipeline Status", "SUCCESS")
        m2.metric("Total Latency", f"{r['total_execution_ms']} ms")
        m3.metric("Output Sink", "Parquet")
        
        st.write(f"**Destination:** `{r['output_destination']}`")
        
        stages = r["stage_latencies_ms"]
        df = pd.DataFrame([
            {"Stage": "Auth & Presign", "Latency (ms)": stages["auth_and_validation"]},
            {"Stage": "Decompress & Extract", "Latency (ms)": stages["extraction_and_decompression"]},
            {"Stage": "Tag & Route", "Latency (ms)": stages["metadata_and_routing"]}
        ])
        fig = px.bar(df, x="Stage", y="Latency (ms)", title="Micro-Stage Latency Breakdown", color="Stage")
        st.plotly_chart(fig, use_container_width=True)

