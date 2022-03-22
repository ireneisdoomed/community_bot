from fastapi import FastAPI

from community_bot.schemas import *

app = FastAPI()

@app.post("/new_post_hook", response_model=NewPost)
async def listener(payload: NewPost):
    print(payload)
    return payload

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


