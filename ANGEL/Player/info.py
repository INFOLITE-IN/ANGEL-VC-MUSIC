from ANGEL.main import bot
from pyrogram import filters


OWNER = [5956449427]
sudos = [5956449427]

@bot.on_message(filters.command("info"))
def info(_, message):
    if message.text == "/info":
        user = message.from_user.id
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    if not message.reply_to_message and message.text != "/info" and user.isnumeric(
    ):
        user = message.text.split(" ")[1]

    if not message.reply_to_message and message.text != "/info" and not user.isnumeric(
    ):
        k = bot.get_users(message.text.split(" ")[1])
        user = k.id

    if user == OWNER:
        status = "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ ᴏᴡɴᴇʀ"

    elif user in sudos:
        status = "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴏɴᴇ ᴏғ ᴍʏ sᴜᴅᴏ ᴜsᴇʀs !"

    else:
        status = "member"

    pfp_count = bot.get_profile_photos_count(user)

    if not pfp_count == 0:
        pfp = bot.get_profile_photos(user, limit=1)
        pfp_ = pfp[0]['thumbs'][0]['file_id']

    foo = bot.get_users(user)
    data = f"""**ғɪʀsᴛ ɴᴀᴍᴇ** : {foo.first_name}
**ʟᴀsᴛ ɴᴀᴍᴇ**: {foo.last_name}
**ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ**: {foo.id}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {foo.mention(foo.first_name)}
**ɪs_ʙᴏᴛ**: {foo.is_bot}
**sᴛᴀᴛᴜs**: {status}
"""

    if pfp_count != 0:
        message.reply_photo(pfp_, caption=data)

    else:
        message.reply_text(data)
