from fastapi import FastAPI
from api.endpoints import prediction

app = FastAPI()

app.include_router(prediction.router)
