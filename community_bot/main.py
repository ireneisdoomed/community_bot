from dotenv import load_dotenv
import os

from fastapi import FastAPI, status
import requests

from community_bot.schemas import *

load_dotenv()

app = FastAPI(
    title="Bot of the Open Targets Community",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Open Targets Community Bot!"}


@app.post("/new_post_hook", response_model=InNewPost, status_code=status.HTTP_200_OK)
async def new_post_hook(payload: InNewPost):
    print(payload)

    return payload


@app.get("/latest_posts", status_code=status.HTTP_200_OK)
async def latest_posts():

    res = get_latest_posts()

    # TODO: Process the response to only return the data we want
    
    return res['topic_list']['topics'][0]

def get_latest_posts():
    """
    Returns the top 200 latest posts from the Discourse API.
    """

    root = 'https://community.opentargets.org/latest.json'
    params = {
        'api_username': os.environ.get('API_USERNAME'),
        'api_key': os.environ.get('API_KEY'),
    }
    return requests.get(root, params=params).json()