from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import get_setting
import platform
import os, sys

system = 'Linux 🐧' if os.name == 'posix' else 'Windows 💻'

if os.name == 'posix':
    if 'termux' in sys.executable.lower():
        system = 'Termux 📱'
    else:
        import distro
        system = distro.name(pretty=False)

default = f'''
<b><a href="https://github.com/purpl3-yt/pyrewrite">PyRewrite</a> - Simple & Convenient</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix.get()}</code><b>"</b>
<b>🖥 OS: {system}</b>
<b>💻 Hosted on: {platform.node()}</b>
<b>🔧 Commands: {str(help_menu.get_lenght())}</b>
<b>📦 Built-in Plugins: {str(help_menu.get_lenght_buildin())}</b>
<b>🔌 Custom Plugins: {str(help_menu.get_lenght_custom())}</b>
<b>🛠 Modules channel: @pyrewrite</b>'''

def get_info_menu(info_type = 'full'):
    if info_type == 'full':
        return default

    elif info_type == 'lite':
        return f'''
<b><a href="https://github.com/purpl3-yt/pyrewrite">PyRewrite</a> Info Menu</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix.get()}</code><b>"</b>
<b>🔧 Commands: {str(help_menu.get_lenght())}</b>
<b>🛠 Modules channel: @pyrewrite</b>'''
    
    elif info_type == 'smaller':
        return f'''
<b><a href="https://github.com/purpl3-yt/pyrewrite">PyRewrite</a></b>
<b>Prefix:</b> <b>"</b><code>{prefix.get()}</code><b>"</b>
'''

    else: 
        return default + '\n\n⛔️ <b>You must set info type (full/lite)!</b>'

@Client.on_message(filters.command('info', prefixes=prefix.get()) & filters.me)
async def info(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    
    info_type = get_setting('info', 'settings', if_option_not_exist='full')

    if info_type != 'smaller':
        if message.reply_to_message != None:
            await client.send_animation(chat_id, get_setting('banner', 'settings'), get_info_menu(info_type), reply_to_message_id=message.reply_to_message.id)
        elif message.reply_to_message == None:
            await client.send_animation(chat_id, get_setting('banner', 'settings'), get_info_menu(info_type))
    
    elif info_type == 'smaller':
        await client.send_message(chat_id, get_info_menu(info_type), disable_web_page_preview=True)

help_menu.add_command('info', 'Get info', 'Get info about userbot')