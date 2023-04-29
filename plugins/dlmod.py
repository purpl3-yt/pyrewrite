from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.restart import restart
import os
#idea by hikka

@Client.on_message(filters.command('dlmod', prefixes=prefix.get()) & filters.me)
async def dlmod(client: Client, message: Message):
    if message.reply_to_message != None:
        if message.reply_to_message.document != None:
            await message.edit('⏳ <b>Downloading...</b>')
            await client.download_media(message.reply_to_message, './plugins/'+os.path.basename(message.reply_to_message.document.file_name))
            await message.edit('✅ <b>Downloaded!</b>')
            await restart(client, message)
        else:
            await message.edit('❌ <b>The message must be a file</b>')
    else:
        await message.edit('❌ <b>Reply to message!</b>')

help_menu.add_command('dlmod', 'download module')