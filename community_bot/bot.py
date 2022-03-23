import os

from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Docs at https://slack.dev/bolt-python/tutorial/getting-started-http#setting-up-your-project