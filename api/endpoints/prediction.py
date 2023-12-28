from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.model_service import ModelService

router = APIRouter()

model_service = ModelService(model_path="models/ml_model.pkl")


class InputData(BaseModel):
    user_id: int
    prev_qual: str
    prev_lgo: float
    month: int
    quarter: int
    year: int


@router.post("/predict")
def get_prediction(data: InputData):
    lgo_prediction = model_service.predict_lgo(data.dict())
    clients_prediction = (2500 - lgo_prediction) / 50
    return {"lgo_prediction": lgo_prediction, "clients_prediction": clients_prediction}
