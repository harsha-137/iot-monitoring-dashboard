# 📡 IoT Monitoring Dashboard

A full-stack real-time IoT dashboard built with **FastAPI**, **MongoDB**, and **Streamlit** to visualize sensor data (temperature, humidity, etc.) from multiple devices. This project is fully containerized using Docker and Docker Compose.

---

## 🏗️ Project Structure

```
iot-monitoring-dashboard/
├── backend/               # FastAPI backend for ingesting and serving sensor data
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/              # Streamlit frontend for real-time visualization
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml     # Compose file to orchestrate backend, frontend, and DB
└── README.md              # You're here
```

---

## 🚀 Features

- 📥 Ingest and store sensor data (from simulated or real IoT devices)
- 📊 Real-time visualization of:
  - Temperature
  - Humidity
- 🔄 Auto-refresh graphs per selected sensor
- 🔍 Select sensor using dropdown
- 🧾 Tabular view of recent readings
- 🐳 Fully containerized (FastAPI + MongoDB + Streamlit)

---

## 📦 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [MongoDB](https://www.mongodb.com/)
- **Containerization:** Docker & Docker Compose

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/harsha-137/iot-monitoring-dashboard.git
cd iot-monitoring-dashboard
```

### 2. Run with Docker Compose

```bash
docker-compose up --build
```

This will:

- Start MongoDB on `localhost:27017`
- Start FastAPI backend on [http://localhost:8000](http://localhost:8000)
- Start Streamlit frontend on [http://localhost:8501](http://localhost:8501)

---

## 📂 API Reference

FastAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

Example endpoint:

```
GET /all-data
Returns last 100 sensor readings
```

---

## 📸 Screenshots

> Add screenshots of your Streamlit dashboard once it's up and running.

---

## 🧪 Simulate Sensor Data (Optional)

You can create a Python script to send mock data to FastAPI like:

```python
import requests
import random
from datetime import datetime

url = "http://localhost:8000/add-data"
sensor_ids = ["sensor-1", "sensor-2", "sensor-3", "sensor-4", "sensor-5"]

for sensor in sensor_ids:
    payload = {
        "device_id": sensor,
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": datetime.utcnow().isoformat()
    }
    requests.post(url, json=payload)
```

---

## 🧹 To Stop & Clean

```bash
docker-compose down -v
```

---

## 🤝 Contributing

Pull requests and suggestions are welcome. For major changes, open an issue first.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Thota Harshavardhan Reddy**  
Senior Software Engineer | Python & IoT Specialist

---