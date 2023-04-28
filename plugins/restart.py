from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import set_setting
import os
@Client.on_message(filters.command('restart', prefixes=prefix.get()) & filters.me)
async def restart(client: Client, message: Message):
    restart_msg = await message.edit('⏳ <b>Restarting userbot...</b>')

    await os.execvp('python3', ['python3','main.py', f'{restart_msg.id},{restart_msg.chat.id}'])

help_menu.add_command('restart', 'Restartes userbot')