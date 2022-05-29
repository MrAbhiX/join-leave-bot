import os
from os import environ
import asyncio
from pyrogram import Client, idle

OWNER_ID = list(
    map(int, os.getenv("OWNER_ID", "").split())
) 
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION_NAME = environ.get("SESSION_NAME", None)

abhi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    plugins=dict(root="Userbot")
    )

abhi.start()
print("[INFO]: PY-TGCALLS CLIENT STARTED !!")

