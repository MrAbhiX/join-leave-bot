import os
import asyncio
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

async def start_bot():
    await bot.start()
    print("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await Abhi.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")

