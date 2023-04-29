from pyrogram.types import Message
import random

def get_args(msg: Message):
    return str(msg.text).split(' ')[1:]

def text_animation(text):
    symbols = ['*', '@', '#', '$', '%', '^', '&', '&']
    temp = text
    temp += temp[:1]
    shif = []
    for i in range(1, len(temp) + 1):
        shif.append(random.choice(symbols))
    steps = []
    phrase = []
    for i in range(1, int(len(temp)) + 1):
        phrase.append(temp[i - 1:i])
    x = 0
    for i in phrase:
        shif.pop(x)
        str = ''.join(shif)
        steps.append(str)
        shif.insert(x, i)
        str = ''.join(shif)
        x += 1
    return steps