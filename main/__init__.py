#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 10433133
API_HASH = "040870a72b1ec7084d572591031491c1"
BOT_TOKEN = "6495082643:AAGouOpO5BT62TgdnC7fYcs6eL9TM2DBFw4"
SESSION = "BQCfMm0AYg82CXgRBe5QPRvksYM6dyWLYgc5pqZSKipbykRztRe8m00k4xLaymyMHjWkuepla1aMdffV5HO52NRAy5WM3iDiicyLU0AbQqBiAoYuPMdt_A_FtRgvPKq5-F2ifWEAMTuDlLHWx4nVRVLAYzyMLkpYEkjI8fd2IRWCRRd98WAFkX4Ug3moYO2QfcDapTu3Tk0nQCdhBbOwGHlYqBsSUkpqdeHHtSlc-b4orXHe-3akjgRMOWrDTcxmJ2g1eYMMGlOaDtqZA4R8QvbDXwtt90t6HHJyOkEYS_zoQdQbYK8zJFjrNg0xI3_n2Mo7LNVhA9D5fDhxuFT6RkAJ24gYIwAAAAF3i9IVAA"
FORCESUB = "ForwardRestrictFile"
AUTH = 6300619285

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
