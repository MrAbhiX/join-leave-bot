import os
import asyncio
from pyrogram import Client, idle

OWNER_ID = list(
    map(int, os.getenv("OWNER_ID", "").split())
) 


Abhi = Client(os.environ["SESSION_NAME"], 
               int(os.environ["API_ID"]), 
               os.environ["API_HASH"],
               plugins=dict(root="Userbot"),
              )






Abhi.run()
print("[INFO]: PY-TGCALLS CLIENT STARTED !!")

