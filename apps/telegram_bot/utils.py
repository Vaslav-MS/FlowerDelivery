import os

def get_bot_token():
    return os.environ.get("TELEGRAM_BOT_TOKEN")

