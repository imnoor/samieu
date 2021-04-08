import json
from pathlib import Path

class Preference:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Preference.__instance == None:
            Preference()
        return Preference.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Preference.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.load()
            Preference.__instance = self

    def load(self):
        data_folder = Path("data/")
        file_to_open = data_folder / "settings.txt"
        with open(file_to_open) as f_check:
            self.data = json.load(f_check)

    def get_program(self):
        return self.data["global"]["program"]

    def get_reload(self):
        return self.data["reload"]
    
    def get_window(self):
        return self.data["global"]["window"]

    def get_timeout(self):
        return self.data["global"]["timeout"]

    def get_commands(self):
        return self.data["commands"]

    def get_stop(self):
        return self.data["stop"]

