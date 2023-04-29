from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import get_args, warn
import random

@Client.on_message(filters.command('get_music', prefixes=prefix.get()) & filters.me)
async def get_music(client: Client, message: Message):

    args = get_args(message)

    try:song_count = args[0]
    except IndexError:
        await warn(message, 'Enter song count!')
        return

    if not song_count.isdigit():
        await warn(message, 'Enter an digit!')
        return
    
    await warn(message, 'Wait...', 'time')
    
    music_list = []

    async for music in client.get_chat_history('@SimplePhonk'):
        if music.audio != None:
            music_list.append(music)
    
    random_music = random.choices(music_list, k=int(song_count))

    for music in random_music:
        await client.forward_messages(message.chat.id, '@SimplePhonk', music.id)

    await warn(message, 'Done!', 'done')

help_menu.add_command('get_music', 'Get music', 'Get music from channels (phonk)')