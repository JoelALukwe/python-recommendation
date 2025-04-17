from fastapi import FastAPI
from .model_registry import ModelRegistry

app = FastAPI()
registry = ModelRegistry()

@app.get("/recommend/{user_id}")
async def recommend(user_id: int):
    model = registry.get_latest_model()
    return model.predict(user_id)
