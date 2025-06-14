import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="IoT Sensor Dashboard", layout="wide")
st.title("📡 IoT Monitoring Dashboard")

API_URL = "http://localhost:8000"

# Step 1: Fetch all sensor IDs once
@st.cache_data(ttl=60)
def fetch_all_data():
    try:
        response = requests.get(f"{API_URL}/all-data")
        if response.status_code == 200:
            data = response.json()["data"]
            df = pd.DataFrame(data)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df.sort_values(by="timestamp", inplace=True)
            return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

full_df = fetch_all_data()

if full_df.empty:
    st.warning("No data available.")
    st.stop()

# Step 2: Dropdown for sensor selection
sensor_ids = full_df["device_id"].unique().tolist()
selected_sensor = st.selectbox("Select Sensor ID", sensor_ids)

# Step 3: Auto-refresh only the selected sensor's data
st_autorefresh(interval=3000, key=f"{selected_sensor}_refresh")

# Step 4: Fetch and display only selected sensor’s data
filtered_df = full_df[full_df["device_id"] == selected_sensor].copy()
filtered_df.set_index("timestamp", inplace=True)

st.subheader(f"📟 Sensor: `{selected_sensor}`")

col1, col2 = st.columns(2)
col1.line_chart(filtered_df["temperature"], height=250, use_container_width=True)
col2.line_chart(filtered_df["humidity"], height=250, use_container_width=True)

# Step 5: Data Table
st.markdown("### 📋 Recent Sensor Readings")
st.dataframe(filtered_df.reset_index().tail(50), use_container_width=True)
