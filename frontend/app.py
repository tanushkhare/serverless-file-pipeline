import streamlit as st
import requests

st.title("🐳 Project 17: Containerization Suite Dashboard")
if st.button("Check Container Health"):
    res = requests.get("http://127.0.0.1:8000/api/status")
    if res.status_code == 200:
        data = res.json()
        st.success(f"Container: {data['container_name']}")
        st.metric("Status", data["status"])
        st.write(f"**Image Tag:** {data['image_tag']}")
        st.write(f"**Port Mapping:** {data['port_mapping']}")