from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args
import contextlib
import io

@Client.on_message(filters.command('eval', prefixes=prefix.get()) & filters.me)
async def eval_cmd(client: Client, message: Message):
    args = get_args(message)
    exc = ''

    try:output = eval(''.join(args))
    except Exception as e:exc = e

    if exc != '':
        await message.edit(f'❌ <b>Error:</b> <code>{exc}' + '</code>')
    else:
        await message.edit(f'✅ <b>Done:</b> <code>{output}' + '</code>')

help_menu.add_command('eval', 'Eval the msg', 'Passes arguments through the eval method')