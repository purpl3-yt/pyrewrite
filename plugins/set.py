from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import get_setting, set_setting
from utils.settings import settings
from plugins.helpers import get_args

@Client.on_message(filters.command('set', prefixes=prefix.get()) & filters.me)
async def set(client: Client, message: Message):
    args = get_args(message)


    try:args[0] # set name
    except:await message.edit('❌ <b>Enter setting!</b>');return

    try:args[1] # set value
    except:await message.edit('❌ <b>Enter setting value!</b>');return
    
    if args[0] == 'prefix':
        set_setting(args[0], args[1], 'main')
    else:
        set_setting(args[0], args[1], 'settings')
    
    await message.edit(f'✅ <b>Set setting:</b> <code>{args[0]}</code> <b>to</b> <code>{args[1]}</code>')

help_menu.add_command('set', 'Set Setting')

@Client.on_message(filters.command('sets', prefixes=prefix.get()) & filters.me)
async def sets(client: Client, message: Message):
    args = get_args(message)

    try:args[0]
    except:
        await message.edit(settings.get())
    else:
        cmd_found = settings.get_by_name(args[0])

        if cmd_found == None:
            await message.edit('❌ <b>Setting not found!</b>')

        else:
            await message.edit(f'<code>{cmd_found}</code> - <b>{cmd_found.get_long_description()}</b>\n<b>Current value:</b> <code>{cmd_found.get_value()}</code>')

help_menu.add_command('sets', 'Get settings', 'Get list of settings')