from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.settings import get_setting
from utils.settings import settings
from plugins.helpers import get_args, text_animation
from pyrogram.errors import FloodWait
from asyncio import sleep

@Client.on_message(filters.command('type', prefixes=prefix.get()) & filters.me)
async def type(client: Client, message: Message):
    text = get_args(message)
    try:
        type_delay = float(get_setting('type_delay', 'settings'))
    except:
        type_delay = 0.05
    for i in text_animation(' '.join(text)):
        try:
            await message.edit(i + '</b>')
        except FloodWait as wait:
            await sleep(wait.value)

        await sleep(type_delay)

@Client.on_message(filters.me)
async def make_type(client: Client, message: Message):
    if get_setting('type', 'settings') == 't':
        message.text = '.type ' + message.text
        await type(client, message)

help_menu.add_command('type', 'Typing animation', 'Make animation when you send message')
settings.add('type', 'typing animation', 'enable .type animation (t, f)', 'f')
settings.add('type_delay', 'how many time to wait (float, with dots)', default_value='0.05')