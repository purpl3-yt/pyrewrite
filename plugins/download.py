from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args
import requests
import os

@Client.on_message(filters.command('download', prefixes=prefix.get()) & filters.me)
async def download_cmd(client: Client, message: Message):
    if message.reply_to_message == None:
        args = get_args(message)
        link = args[0]
        
        await message.edit('⏳ <b>Downloading...</b>')
        
        try:file = requests.get(link).content
        except Exception as e:
            await message.edit(f'❌ <b>Error:</b> <code>{e}</code>')
            return
        file_name = os.path.basename(link)

        with open(file_name, 'wb') as s:
            s.write(file)

        await message.edit('✅ <b>Downloaded!</b>')

        await client.send_document(message.chat.id, file_name)

        os.remove(file_name)

    elif message.reply_to_message != None:
        if message.reply_to_message.text != None:
            link = message.reply_to_message.text

            if link.startswith('https'):

                if link.endswith('/'):
                    link = link[:-1]

                file_name = os.path.basename(link)

                if file_name == '':
                    file_name = 'unknown'

                await message.edit('⏳ <b>Downloading...</b>')
        
                file = requests.get(link).content


                with open(file_name, 'wb') as s:
                    s.write(file)

                await message.edit('✅ <b>Downloaded!</b>')

                await client.send_document(message.chat.id, file_name)

                os.remove(file_name)

help_menu.add_command('download', 'Download by link', 'Download and send file by link')