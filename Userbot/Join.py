from pyrogram import Client, filters

from pyrogram.errors import UserAlreadyParticipant

import asyncio
from main import abhi



@Client.on_message(filters.command("join") & ~filters.private & ~filters.bot)


async def join_group(client, message):
    semx = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(semx)
    except:
        await message.reply_text(
            "• **i'm not have permission:**\n\n» ❌ __Add Users__",
        )
        return

    try:
        user = await abhi.get_me()
    except:
        user.first_name = "abhi userbot"

    try:
        await abhi.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 Flood Wait Error 🛑 \n\n**userbot couldn't join your group due to heavy join requests for userbot**"
            "\n\n**or add assistant manually to your Group and try again**",
        )
        return
    await message.reply_text(
        f"✅ **userbot succesfully entered chat**",
    )
