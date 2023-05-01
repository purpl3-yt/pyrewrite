from utils.prefix import prefix

class Command:
    def __init__(self, name, description_short, description_long, usage, author) -> None:
        self.name = name
        self.description_short = description_short
        self.description_long = description_long
        self.usage = usage
        self.author = author

    def get_name(self):
        return self.name

    def get_long_description(self):
        return self.description_long
    
    def get_short_description(self):
        return self.description_short
    
    def get_usage(self):
        return self.usage

    def get_author(self):
        return self.author

    def __str__(self):
        return self.name
    
class Help_Menu:
    commands = {}

    def __init__(self) -> None:
        pass

    def add_command(self, name, description_short = 'simple command', description_long = None, usage = 'Not set', author = 'Not set'):
        if description_long == None:
            description_long = description_short

        self.commands[name] = [name, Command(name, description_short, description_long, usage, author)]

    def get(self):
        help_text = '<b>PyRewrite modules</b>\n'

        for command in self.commands.values():
            command_name = command[0]
            command_description_short = command[1].get_short_description()

            help_text += f'<code>{prefix.get()}{command_name}</code><b> - {str(command_description_short).capitalize()}</b>\n'
            
 
        return help_text
        
    def get_lenght(self):
        return len(self.commands.items())
    
    def get_by_name(self, query):
        for command in self.commands.values():
            if command[1].get_name() == query:
                return command[1]
        
        return None

help_menu = Help_Menu()