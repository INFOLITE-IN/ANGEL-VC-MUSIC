 import asyncio
from config import BOT_USERNAME, SUDO_USERS
from ANGEL.decorators import authorized_users_only, sudo_users_only, errors
from ANGEL.filters import command, other_filters
from ANGEL.main import user as USER
from pyrogram import filters
from ANGEL.main import bot as Client
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **ɪ'ᴍ ɴᴏᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ:**\n\n» ❌ __ᴀᴅᴅ ᴜsᴇʀs__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ 🛑 \n\n**ᴜsᴇʀʙᴏᴛ ᴄᴏᴜʟᴅɴ'ᴛ ᴊᴏɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴜᴇ ᴛᴏ ʜᴇᴀᴠʏ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs ғᴏʀ ᴜsᴇʀʙᴏᴛ**"
            "\n\n**ᴏʀ ᴀᴅᴅ ᴀssɪsᴛᴀɴᴛ ᴍᴀɴᴜᴀʟʟʏ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ**",
        )
        return
    await message.reply_text(
        f"✅ **ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇsғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴄʜᴀᴛ**",
    )


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛ")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **ᴜsᴇʀʙᴏᴛ ᴄᴏᴜʟᴅɴ'ᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴍᴀʏ ʙᴇ ғʟᴏᴏᴅᴡᴀɪᴛs.**\n\n**» ᴏʀ ᴍᴀɴᴜᴀʟʟʏ ᴋɪᴄᴋ ᴜsᴇʀʙᴏᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ**"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **ᴜsᴇʀʙᴏᴛ** ʟᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴀʟʟ ɢʀᴏᴜᴘ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ...\n\nʟᴇғᴛ: {left} ᴄʜᴀᴛs.\nғᴀɪʟᴇᴅ: {failed} ᴄʜᴀᴛs."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ ʟᴇғᴛ ғʀᴏᴍ: {left} ᴄʜᴀᴛs.\n❌ ғᴀɪʟᴇᴅ ɪɴ: {failed} ᴄʜᴀᴛs."
    )
