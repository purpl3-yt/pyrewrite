from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
import os

@Client.on_message(filters.command('info', prefixes=prefix.get()) & filters.me)
async def info(client: Client, message: Message):
    system = 'Linux 🐧' if os.name == 'posix' else 'Windows 💻'
    if os.name == 'posix':
        import distro
        system = distro.name(pretty=False)
    await message.edit(f'''
<b>PyRewrite - Simple & Convenient</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix.get()}</code><b>"</b>
<b>🖥 OS: {system}</b>
<b>🔧 Commands: {str(help_menu.get_lenght())}</b>
''')

help_menu.add_command('info', 'Get info', 'Get info about userbot')