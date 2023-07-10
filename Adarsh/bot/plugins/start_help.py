#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
from pyrogram.types import ReplyKeyboardMarkup
from ...utils.db_helpers import add_user_to_database

db = Database(Var.DATABASE_URL, Var.name)

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    await add_user_to_database (b, m)
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/8e67ae4a3803f69a28218.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀᴢ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"), InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")],
                    [InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://youtube.com/@itzjeol")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>❖ YouTube.com/@itzjeol</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )

@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(b, m):
    await add_user_to_database (b, m)
              
    await m.reply_photo(
            photo=WELCOM_IMG,
            caption=HELP_MSG, 
            reply_markup=HELP_BUTTONS
        )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(b, m):
    await add_user_to_database (b, m)
    await m.reply_photo(
            photo=WELCOM_IMG,
            caption=ABOUT_MSG,
            reply_markup=ABOUT_BUTTONS,
            
        )
    
WELCOM_IMG = "https://graph.org/file/8e67ae4a3803f69a28218.jpg"

HELP_MSG = """
--> Send me any file/Video , I will send you a link to download it!
--> You can Stream/Download from our webpage!
--> Add me in your Channel to get Stream/Download links!
"""

HELP_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"),
    InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support"),
    ],[
    InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"),
    InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")
    ],[
    InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://youtube.com/@itzjeol")
    ]]
)

ABOUT_MSG = """
Bot Name : 
Language : 
Library :
Bot Creator :
Updates Channel : 
Support Group : 
Youtube :
"""
ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/beta_botz"),
    InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/beta_support"),
    ],[
    InlineKeyboardButton("OWNER", url="https://t.me/jeol_tg"),
    InlineKeyboardButton("💠 DEVELOPER", url="https://github.com/Adarsh-Goel")
    ],[
    InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://youtube.com/@itzjeol")
    ]]
)


