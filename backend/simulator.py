import time
import requests
import random
from datetime import datetime, UTC

def simulate():
    while True:
        for sensor in ["sensor_001", "sensor_002", "sensor_003", "sensor_004", "sensor_005"]:
            data = {
                "device_id": sensor,
                "temperature": round(random.uniform(20, 35), 2),
                "humidity": round(random.uniform(30, 60), 2),
                "timestamp": datetime.now(UTC).isoformat()
            }
            try:
                res = requests.post("http://localhost:8000/data", json=data)
                print(res.json())
            except Exception as e:
                print("Error sending data:", e)
            time.sleep(1)

if __name__ == "__main__":
    simulate()
