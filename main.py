import os

from pyrogram import Client


Abhi = Client(os.environ["SESSION_NAME"], 
               int(os.environ["API_ID"]), 
               os.environ["API_HASH"])



