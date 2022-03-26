from fastapi import FastAPI, status

from community_bot.schemas import *

app = FastAPI()


@app.post("/new_post_hook", response_model=InNewPost, status_code=status.HTTP_200_OK)
async def listener(payload: InNewPost):
    print(payload)
    '''
    title = payload['title']

    if title == 'test':
        prediction = model.predict(title)
    
    req = {
        "prediction": prediction,
    }

    requests.req(endpoint_slack)
    '''
    return payload


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
