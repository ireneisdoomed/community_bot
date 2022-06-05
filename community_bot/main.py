from fastapi import FastAPI, status

from community_bot.schemas import *

app = FastAPI()


@app.post("/new_post_hook", response_model=InNewPost, status_code=status.HTTP_200_OK)
async def new_post_hook(payload: InNewPost):
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


@app.get("/greet/{name}")
async def say_hi(name: str):
    return {"greeting": f'hi {name}'}
