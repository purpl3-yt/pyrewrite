from pyrogram import Client
from configparser import ConfigParser
import os, sys
from utils.config import *
import pip
import logging
import sys

os.chdir(sys.path[0])

requirements = [
    'install',
    'pyrogram==2.0.104',
    '--upgrade'
]

pip.main(requirements)

logging.basicConfig(level=logging.INFO, format='%(message)s')

if not os.path.isfile('config.ini'): # if config doesn't exist
    with open('config.ini', 'w') as cfg:cfg.write('[main]') # create config
    config = ConfigParser()
    config.read('config.ini')
    config.set('main', 'api_id', 'ENTER_YOUR_API_ID')
    config.set('main', 'api_hash', 'ENTER_YOUR_API_HASH')
    config.set('main', 'prefix', '.')
    config.add_section('settings')

    with open('config.ini', 'w') as cfg:config.write(cfg)

    print('Created config, please enter your api_id and api_hash!')
    quit()

if get_setting('api_id') == 'ENTER_YOUR_API_ID' or get_setting('api_hash') == 'ENTER_YOUR_API_HASH':
    print('Please enter your api_id and api_hash!')
    quit()

client = Client(
    'pyrewrite',
    api_id=get_setting('api_id'),
    api_hash=get_setting('api_hash'),
    device_model='PyRewrite',
    plugins=dict(root='plugins'),
)

try:sys.argv[1]
except IndexError:pass
else:
    sys_args = sys.argv[1].split(',')
    message_id = sys_args[0]
    chat_id = sys_args[1]

    with client:
        client.edit_message_text(int(chat_id), int(message_id), '✅ <b>Restarted!</b>')

logo = '''
  ______   ______  _______        ______  ___ _____ _____ 
 |  _ \ \ / /  _ \| ____\ \      / /  _ \|_ _|_   _| ____|
 | |_) \ V /| |_) |  _|  \ \ /\ / /| |_) || |  | | |  _|  
 |  __/ | | |  _ <| |___  \ V  V / |  _ < | |  | | | |___ 
 |_|    |_| |_| \_\_____|  \_/\_/  |_| \_\___| |_| |_____|
                                                          '''

print(logo)

client.run()