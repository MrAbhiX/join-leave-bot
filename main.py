import os
from os import environ
import asyncio
import aiohttp
from Python_ARQ import ARQ
from pyrogram import Client, idle

OWNER_ID = list(
    map(int, os.getenv("OWNER_ID", "").split())
) 
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION_NAME = environ.get("SESSION_NAME", None)
ARQ_API_URL = environ.get("ARQ_API_URL", None)
ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))

abhi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    plugins=dict(root="Userbot")
    )

async def main():
    global arq
    session = aiohttp.ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

    await abhi.start()
    await abhi.send_message(LOG_GROUP_ID, "I'm ChatBot Message Me For Chat With Me")
    print(
        """
-----------------
| ChatBot Assistant Started Made By Abhi! |
-----------------
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())

