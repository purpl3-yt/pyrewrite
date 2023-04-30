from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import warn

@Client.on_message(filters.command('quit', prefixes=prefix.get()) & filters.me)
async def quit_cmd(client: Client, message: Message):
    await message.edit('👋 <b>Userbot stopped, Bye-bye!</b>')
    quit()

help_menu.add_command('quit', 'Quit from userbot')