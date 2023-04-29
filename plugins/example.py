from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu

@Client.on_message(filters.command('exm', prefixes=prefix.get()) & filters.me)
async def exm(client: Client, message: Message):
    await message.edit('example command')