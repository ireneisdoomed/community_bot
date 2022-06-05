
## Set up
```bash
# Create environment
conda create -n bot python=3.10 
conda activate bot

# TODO: Instructions to install dependencies
```

## Spin up

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

# To expose the localhost URL publically
./ngrok  http <PORT NUMBER>
```