from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import warn
import os

@Client.on_message(filters.command('neofetch', prefixes=prefix.get()) & filters.me)
async def neofetch(client: Client, message: Message):
    await warn(message, 'Wait...', 'time')
    await message.edit('<code>' + os.popen('neofetch --stdout').read() + '</code>')

help_menu.add_command('neofetch', 'send neofetch')