from utils.config import set_setting, get_setting

class Prefix:
    def __init__(self) -> None:
        pass

    def get(self):
        return get_setting('prefix')
    
    def set(self, new):
        set_setting('prefix', new)

prefix = Prefix()