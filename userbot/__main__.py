
import sys
from importlib import import_module
from platform import python_version

import requests
from pytgcalls import __version__ as pytgcalls
from pytgcalls import idle
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon import version


from buserot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from Bonten import CMD_HANDLER as cmd
from Bonten import DEVS, LOGS, blacklistBonten, bot, branch, call_py
from Bonten.modules import ALL_MODULES
from Bonten.utils import autobot, checking

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    name = user.first_name
    uid = user.id
    blacklistBonten = requests.get(
        "https://raw.githubusercontent.com/BontenXd/Reforestation/master/Bontenblacklist.json"
    ).json()
    if user.id in blacklistBonten:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, Bontennya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
    if 1700405732 not in DEVS:
        LOGS.warning(
            f"EOL\nBonten-Bonten v{BOT_VER}, Copyright © 2021-2022 𝙰𝚈𝙸𝙸𝙽𝚇𝙳• <https://github.com/BontenXd>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("Bonten.modules." + module_name)
    
LOGS.info(f"Python Version - {python_version()}")
LOGS.info(f"Telethon Version - {version.__version__}")
LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")

LOGS.info(
    f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
)

LOGS.info(f"Bonten-Bonten Version - {BOT_VER} [✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙳𝙸𝙰𝙺𝚃𝙸𝙵𝙺𝙰𝙽 ✧]")

LOGS.info(
    f"Jika {name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/BontenXdSupport"
)

async def Bonten_Bonten_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"**✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**\n**✧ 𝙱𝙴𝚁𝙷𝙰𝚂𝙸𝙻 𝙳𝙸 𝙰𝙺𝚃𝙸𝙵𝙺𝙰𝙽 ✧**\n━━\n➠ **𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 -** `{BOT_VER}`\n➠ `@{branch}`\n➠ **𝙺𝙴𝚃𝙸𝙺** `{cmd}alive` **𝚄𝙽𝚃𝚄𝙺 𝙼𝙴𝙽𝙶𝙴𝙲𝙴𝙺 𝙱𝙾𝚃**\n━━\n➠ **𝙼𝙰𝙽𝙰𝙶𝙴𝙳 𝙱𝚈** : {name}",
            )

    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@BontenXdSupport"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(Bonten_Bonten_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
