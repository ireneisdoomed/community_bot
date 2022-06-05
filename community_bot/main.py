from datetime import datetime
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


@app.post("/new_post_hook", response_model=InNewTopic, status_code=status.HTTP_200_OK)
async def new_post_hook(payload: InNewTopic):
    print(payload)

    return payload


@app.get("/latest_posts", response_model=OutUnansweredTopics, status_code=status.HTTP_200_OK)
async def latest_posts():

    latest_input = get_latest_posts()
    unanswered_posts = []

    for post in latest_input['topic_list']['topics']:
        # Only add posts that have not been answered yet
        if post["reply_count"] == 0 or post["highest_post_number"] == 1:

            unanswered_posts.append({
                "title": post["title"],
                "date": post["created_at"][:10],
                "tags": post["tags"],
            })

    latest_output = {
        "count": len(unanswered_posts),
        "posts": unanswered_posts}
    
    return latest_output

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