import os
import asyncio
from pyrogram import Client, idle

OWNER_ID = list(
    map(int, os.getenv("OWNER_ID", "").split())
) 


abhi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    plugins=dict(root="Userbot")
    )

abhi.start()
print("[INFO]: PY-TGCALLS CLIENT STARTED !!")

