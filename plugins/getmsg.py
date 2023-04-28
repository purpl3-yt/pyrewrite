from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args

@Client.on_message(filters.command('getmsg', prefixes=prefix.get()) & filters.me)
async def getmsg(client: Client, message: Message):
    try:get_args(message)[0]
    except IndexError:print(message);await message.edit('✅ <b>Done!</b>')
    else:await message.edit(f'✅ <b>Done</b>: <code>{message}</code>')

help_menu.add_command('getmsg', 'Get message data', 'Send all message data to terminal (json, pyrogram)')