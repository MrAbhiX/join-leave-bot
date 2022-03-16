import os

from pyrogram import Client


Abhi = Client(os.environ["SESSION_NAME"], 
               int(os.environ["API_ID"]), 
               os.environ["API_HASH"])



bot = Client(
    "userbot Join-Leave Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

Abhi.start()
bot.run()
