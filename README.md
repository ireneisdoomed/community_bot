I want to automatise the assingment of questions in the [Open Targets Community](https://community.opentargets.org) to the different teams. This will be done by categorising every new topic that someone posts.
At the same time, I want to facilitate tracking what are the questions that still need an answer.

This will be packaged in the form of a Slack bot.
## API Endpoints
`new_post_hook` is currently in development.

- `/`:
  - `GET`:
    - `description`: Returns a welcome to the API message.
    - `responses`:
      - `200`:
        - `schema`:
          - `type`: object
          - `example`: {"message": "Welcome to the Open Targets Community Bot!"}
- `unanswered`:
  - `GET`:
    - `description`: Returns an object with a list of unanswered questions.
    - `responses`:
      - `200`:
        - `schema`:
          - `type`: object
          - `example`: {"count":1,"posts":[{"title":"Aging-associated genes compiled from literature","date":"2022-06-05","tags":[]}
- `new_post_hook`:
  - `POST`:
    - `description`: Listener for whenever a new topic is created. This will be later processed to categorise the new topic and assign it to a team.

## Installation
### Set up
```bash
# Create environment
conda create -n bot python=3.10 
conda activate bot

# TODO: Instructions to install dependencies
```

### Spin up

```bash
uvicorn community_bot.api:app --reload 

# To test the endpoint
curl -X 'POST' \
  'http://b008-47-62-148-25.ngrok.io/webhook' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
      "login": "defunkt",
      "id": 2,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://avatars.githubusercontent.com/u/2?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/defunkt",
      "html_url": "https://github.com/defunkt"
}'

# To expose the localhost URL publically - download ngrok from https://ngrok.com/download
./ngrok  http <PORT NUMBER>
```

