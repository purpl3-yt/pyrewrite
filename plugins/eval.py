from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args, warn

@Client.on_message(filters.command('eval', prefixes=prefix.get()) & filters.me)
async def eval_cmd(client: Client, message: Message):
    args = get_args(message)
    exc = ''

    try:output = eval(''.join(args))
    except Exception as e:exc = e

    if exc != '':
        await warn(message, f'<b>Error:</b> <code>{exc}' + '</code>', raw=True)
    else:
        await warn(message, f'<b>Done:</b> <code>{output}' + '</code>', 'done', True)

help_menu.add_command('eval', 'Eval the msg', 'Passes arguments through the eval method', f'{prefix.get()}eval 2+2\n{prefix.get()}eval print("Hello World!")')