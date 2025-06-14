from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models import SensorData
from mongo_layer import sensor_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "IoT Monitoring Backend"}


@app.post("/data")
async def receive_data(data: SensorData):
    sensor_collection.insert_one(data.model_dump())
    return {"status": "received"}

@app.get("/all-data")
async def get_all_data():
    docs = sensor_collection.find().sort("timestamp", -1).limit(100)
    data = []
    for doc in docs:
        doc["_id"] = str(doc["_id"])
        if "timestamp" in doc:
            doc["timestamp"] = doc["timestamp"].isoformat()
        data.append(doc)
    return JSONResponse(content={"data": data})
