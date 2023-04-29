from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args, warn

@Client.on_message(filters.command('getmsg', prefixes=prefix.get()) & filters.me)
async def getmsg(client: Client, message: Message):
    try:get_args(message)[0]
    except IndexError:
        print(message)
        await warn(message, 'Done!', 'done')
    else:
        await warn(message, f'✅ <b>Done</b>: <code>{message}</code>', 'done', True)

help_menu.add_command('getmsg', 'Get message data', 'Send all message data to terminal (json, pyrogram)')