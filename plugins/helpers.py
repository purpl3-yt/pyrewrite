from pyrogram.types import Message

def get_args(msg: Message):
    return str(msg.text).split(' ')[1:]