from lib.analytics import Analtyics
from pywinauto.actionlogger import reset_level
from lib.preference import Preference
import time
import random

class Command:
    def __init__(self, appWindow):
        self.commands= Preference().get_commands()
        self.appWindow = appWindow

    def refresh(self):
        Preference.getInstance().load()
        self.commands= Preference().get_commands()

    def process(self,args : str):
        cmds = args.split(sep=" ")
        #print(args)
        for command in cmds:
            if command in self.commands:
                #print(command)
                code = self.translate(command)
                print('Sending Code :' + code)
                time.sleep(random.random())
                self.appWindow.type_keys("{" + code + " down}")
                time.sleep(random.random())
                self.appWindow.type_keys("{" + code + " up}")
                #self.appWindow.TypeKeys(code)

    def translate(self,cmd):
        retVal  = self.commands[cmd]
        if not retVal:
            Analtyics.getInstance().log_fail(cmd)
        else:
            Analtyics.getInstance().log_wins(cmd)
        return retVal
        

