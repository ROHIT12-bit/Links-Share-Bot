# +++ Modified By [telegram username: @Codeflix_Bots
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8459870354:AAEj6V3xEtBkTvYQ3nDOvR2Ks2uEYid3B0o")
APP_ID = int(os.environ.get("APP_ID", "20366634"))
API_HASH = os.environ.get("API_HASH", "72095ec36984aa9ceb0dbaa9cec31559")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "7845335174"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://botskingdom1:gf3vWBaZi5hKwWd0@cluster0.7tu4jk0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "link")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", """<blockquote>𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐝𝐞𝐯𝐢𝐥 𝐟𝐫𝐮𝐢𝐭 𝐮𝐬𝐞𝐫!</blockquote>
<blockquote>𝐈’𝐌 𝐘𝐎𝐔𝐑 𝐋𝐈𝐍𝐊 𝐒𝐇𝐀𝐑𝐄 𝐁𝐎𝐓, 𝐀𝐍𝐃 𝐉𝐔𝐒𝐓 𝐋𝐈𝐊𝐄 𝐌𝐎𝐍𝐊𝐄𝐘 𝐃. 𝐋𝐔𝐅𝐅𝐘, 𝐈 𝐊𝐄𝐄𝐏 𝐓𝐇𝐈𝐍𝐆𝐒 𝐒𝐈𝐌𝐏𝐋𝐄.</blockquote>
<blockquote>𝐒𝐄𝐍𝐃 𝐌𝐄 𝐀𝐍𝐘 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐈’𝐋𝐋 𝐓𝐔𝐑𝐍 𝐈𝐓 𝐈𝐍𝐓𝐎 𝐀 𝐂𝐋𝐄𝐀𝐍, 𝐅𝐀𝐒𝐓, 𝐒𝐇𝐀𝐑𝐄𝐀𝐁𝐋𝐄 𝐋𝐈𝐍𝐊!</blockquote>
<blockquote>𝐒𝐎 𝐂𝐎𝐌𝐄 𝐎𝐍 𝐍𝐀𝐊𝐀𝐌𝐀 — 𝐃𝐑𝐎𝐏 𝐘𝐎𝐔𝐑 𝐅𝐈𝐑𝐒𝐓 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐋𝐄𝐓’𝐒 𝐒𝐄𝐓 𝐒𝐀𝐈𝐋 𝐓𝐎 𝐓𝐇𝐄 𝐆𝐑𝐀𝐍𝐃 𝐋𝐈𝐍𝐄 𝐎𝐅 𝐋𝐈𝐍𝐊𝐒! 🌊🏴‍☠️</blockquote>
<blockquote>🌊 𝐁𝐚𝐜𝐤𝐞𝐝 𝐛𝐲 <a href='https://t.me/Botskingdoms'>✦ 𝗕𝗢𝗧𝗦 𝗞𝗜𝗡𝗚𝗗𝗢𝗠𝗦 ✦</a></blockquote>""")
HELP = os.environ.get("HELP_MESSAGE", "𝐍𝐎𝐓𝐇𝐈𝐍𝐆 𝐀𝐁𝐎𝐔𝐓 𝐌𝐄\n\n𝐉𝐮𝐬𝐭 𝐟𝐮𝐜𝐤 𝐨𝐟 𝐦𝐚𝐧[𝐌𝐟]")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by 𝐁𝐎𝐓𝐒𝐊𝐈𝐍𝐆𝐃𝐎𝐌𝐒 + 𝐀𝐈 to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜғʟɪx</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/codeflix_bots'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/cosmic_freak'>ʏᴀᴛᴏ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProYato</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/animes_cruise'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movieflixspot'>ᴍᴏᴠɪᴇғʟɪx sᴘᴏᴛ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/webseries_flix'>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/hanime_arena'>ᴄᴏʀɴʜᴜʙ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornhwa_flix'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜғʟɪx</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProYato</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003280198213")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7845335174").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
