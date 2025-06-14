from pydantic import BaseModel
from datetime import datetime, UTC

class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    timestamp: datetime = datetime.now(UTC)