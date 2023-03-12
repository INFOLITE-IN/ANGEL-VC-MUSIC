 import logging
from config import BOT_USERNAME
from ANGEL.filters import command, other_filters
from ANGEL.main import bot as Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🗑 ᴄʟᴏsᴇ", callback_data="cls",
                )
            ]
        ]
    )

    try:
        if len(message.command) < 2:
            await message.reply_text("/search **ɴᴇᴇᴅs ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ !**")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎 **sᴇᴀʀᴄʜɪɴɢ...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"🏷 **ɴᴀᴍᴇ:** __{results[i]['title']}__\n"
            text += f"⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{results[i]['duration']}`\n"
            text += f"👀 **ᴠɪᴇᴡs:** `{results[i]['views']}`\n"
            text += f"📣 **ᴄʜᴀɴɴᴇʟ:** {results[i]['channel']}\n"
            text += f"🔗: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
