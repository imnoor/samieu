from lib.preference import Preference
from lib.voice import VoiceServer
from lib.command import Command
from pywinauto.application import Application

prg = Preference.getInstance().get_program()
app = Application().start(prg)
win = Preference.getInstance().get_window()
print(win)
cmd = Command(getattr(app,win ))
server = VoiceServer()
server.listen(cmd)

