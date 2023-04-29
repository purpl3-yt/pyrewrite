from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import get_setting
import os, sys

@Client.on_message(filters.command('info', prefixes=prefix.get()) & filters.me)
async def info(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    system = 'Linux 🐧' if os.name == 'posix' else 'Windows 💻'
    if os.name == 'posix':
        if 'termux' in sys.executable.lower():
            system = 'Termux 📱'
        else:
            import distro
            system = distro.name(pretty=False)

    await client.send_animation(chat_id, get_setting('banner', 'settings'), f'''
<b>PyRewrite - Simple & Convenient</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix.get()}</code><b>"</b>
<b>🖥 OS: {system}</b>
<b>🔧 Commands: {str(help_menu.get_lenght())}</b>
''')

help_menu.add_command('info', 'Get info', 'Get info about userbot', author='Purpl3')