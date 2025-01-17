
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from Bonten import BOT_USERNAME
from Bonten import CMD_HANDLER as cmd
from Bonten import bot
from Bonten.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="helpme")
async def _(event):
    if event.fwd_from:
        return
    if BOT_USERNAME is not None:
        chat = "@Botfather"
        try:
            results = await event.client.inline_query(BOT_USERNAME, "@AyiinXdSupport")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            xx = await edit_or_reply(
                event,
                "**Inline Mode Tidak aktif.**\n__Sedang Menyalakannya, Harap Tunggu Sebentar...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(BOT_USERNAME)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message("Search")
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    await event.client(UnblockRequest(chat))
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(BOT_USERNAME)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message("Search")
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                await xx.edit(
                    f"**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `{cmd}helpme` **lagi untuk membuka menu bantuan.**"
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await edit_or_reply(
            event,
            "**Silahkan Buat BOT di @BotFather dan Tambahkan Var** `BOT_TOKEN` & `BOT_USERNAME`",
        )
