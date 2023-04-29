from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args, warn
import os
import pyrogram.errors

@Client.on_message(filters.command('terminal', prefixes=prefix.get()) & filters.me)
async def exm(client: Client, message: Message):
    args = get_args(message)
    
    await warn(message, 'Executing...', 'time')

    output = os.popen(' '.join(args)).read()
    
    try:
        await warn(message, '<b>Done:</b> <code>\n' + output + '</code>', 'done', True)

    except pyrogram.errors.exceptions.bad_request_400.MessageTooLong:
        await warn(message, 'Error: Message to long!\nSending as file...')
        
        with open('./output.txt', 'w', encoding='1251') as out:
            out.write(output)
        
        await client.send_document(message.chat.id, './output.txt')
        
        os.remove('./output.txt')

help_menu.add_command('terminal', 'Terminal output', 'Send you output from terminal')