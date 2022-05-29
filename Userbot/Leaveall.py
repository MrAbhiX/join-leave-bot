import asyncio
from pyrogram import Client, filters
from main import OWNER_ID
from main import Abhi


@Client.on_message(filters.command(["userbotleaveall", "leaveall"]) & filters.user(OWNER_ID))
async def leaveall(client, message):
    if message.from_user.id not in OWNER_ID:
        return

    left = 0
    failed = 0
    lol = await message.reply("Assistant Leaving all chats")
    async for dialog in Abhi.iter_dialogs():
        try:
            await Abhi.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Assistant leaving all group... \n\nLeft: {left} chats. Failed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
