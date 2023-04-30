from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args, warn

@Client.on_message(filters.command('help', prefixes=prefix.get()) & filters.me)
async def info(client: Client, message: Message):
    args = get_args(message)

    try:args[0]
    except:
        await message.edit(help_menu.get())
    else:
        cmd_found = help_menu.get_by_name(args[0])
        if cmd_found == None:
            await warn(message, 'Command not found!')

        else:
            await message.edit(f'<code>{prefix.get()}{cmd_found}</code> - <b>{cmd_found.get_long_description()}\nUsage: </b>\n{cmd_found.get_usage()}\n<b>Author: {cmd_found.get_author()}</b>')