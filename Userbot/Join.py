from pyrogram import Client, filters
from main import command
from pyrogram.errors import UserAlreadyParticipant
from decoraters import authorized_users_only, errors
import asyncio
from main import Abhi



@Client.on_message(command("join") & ~filters.private & ~filters.bot)

@authorized_users_only
@errors
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
        user = await Abhi.get_me()
    except:
        user.first_name = "abhi userbot"

    try:
        await Abhi.join_chat(invitelink)
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
