import os

from pyrogram import Client, idle

OWNER_ID = list(
    map(int, os.getenv("OWNER_ID", "").split())
) 


Abhi = Client(os.environ["SESSION_NAME"], 
               int(os.environ["API_ID"]), 
               os.environ["API_HASH"])



bot = Client(
    "userbot Join-Leave Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    plugins=dict(root="Userbot"),
)

Abhi.start()
bot.run()
idle()
