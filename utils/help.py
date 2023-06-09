from utils.prefix import prefix
import os

class Command:
    def __init__(self, name, description_short, description_long, usage) -> None:
        self.name = name
        self.description_short = description_short
        self.description_long = description_long
        self.usage = usage

    def get_name(self):
        return self.name

    def get_long_description(self):
        return self.description_long
    
    def get_short_description(self):
        return self.description_short
    
    def get_usage(self):
        return self.usage

    def __str__(self):
        return self.name
    
class Help_Menu:
    commands = {}

    def __init__(self) -> None:
        pass

    def add_command(self, name, description_short = 'simple command', description_long = None, usage = 'Not set'):
        if description_long == None:
            description_long = description_short

        self.commands[name] = [name, Command(name, description_short, description_long, usage)]

    def get(self):
        help_text = '<b>PyRewrite modules</b>\n'

        for command in self.commands.values():
            command_name = command[0]
            command_description_short = command[1].get_short_description()

            help_text += f'<code>{prefix.get()}{command_name}</code><b> - {str(command_description_short).capitalize()}</b>\n'''
            
 
        return help_text
        
    def get_lenght(self):
        return len(self.commands.items())
    
    def get_by_name(self, query):
        for command in self.commands.values():
            if command[1].get_name() == query:
                return command[1]
        
        return None
    
    def get_lenght_buildin(self):
        return len([m for m in os.listdir('plugins') if m not in ['custom', '__pycache__', 'helpers.py']])

    def get_lenght_custom(self):
        return len([m for m in os.listdir('plugins/custom') if m not in ['__pycache__']])

help_menu = Help_Menu()