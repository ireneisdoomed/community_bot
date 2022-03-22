from fastapi import FastAPI
from pydantic import BaseModel

# TODO: Specify response model

app = FastAPI()

@app.post("/webhook")
async def listener(payload: dict[str, dict]):
    print(payload)
    return payload

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


