from configparser import ConfigParser
import configparser

config = ConfigParser()
config.read('config.ini')

def read_config():
    global config
    config = ConfigParser()
    config.read('config.ini')


def write_config():
    with open('config.ini', 'w') as cfg:config.write(cfg)

def set_setting(key, value, section = 'main'):
    try:config.set(section, key, value)
    except configparser.NoSectionError:
        config.add_section(section)
        config.set(section, key, value)
        write_config()
        return
    
    write_config()
    
def get_setting(key, section = 'main', if_option_not_exist = None):
    try:
        return config.get(section, key)
    except configparser.NoOptionError:
        set_setting(key, if_option_not_exist, section)
        return config.get(section, key)