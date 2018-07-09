import sys
import os
import pyautogui
import time
import imp
from awlib.autoit import *

class TextArea(object):
    buffer = []
    def __init__(self):
        self.buffer = []
    def write(self, *args, **kwargs):
        self.buffer.append(args)
    def clear(self):
        self.buffer = []
    def show(self):
        print buffer

cmd_list=['clr\r', 'perr\r', 'pall\r']

def automate_putty(args):
    app = args[0].getApp()
    com = args[1]
    putty = app.PuttyConfiguration

    #save putty control info
    stdout = sys.stdout
    sys.stdout = TextArea()
    putty.print_control_identifiers()
    winspec=sys.stdout
    sys.stdout = stdout;

    left_offset = 5
    down_offset = 5
    saved_session=[]
    for tup in winspec.buffer:
        if tup[0].find('Saved Sessions') > -1:
            saved_session.append(tup)

    locate=[]
    for session in saved_session:
        if session[0].find('Edit') > -1:
            grid =session[0][session[0].find('(')+1:session[0].find(')')].split(',')
            for pos in grid:
                pos=pos.strip()
                locate.append(int(pos[1:]))
            pyautogui.moveTo(locate[0]+left_offset, locate[1]+down_offset)
            pyautogui.click(button='right')

    putty.Edit3.type_keys(com)
    putty.Load.click()
    putty.Open.click()
    com_app=app.PuTTY
    com_app.type_keys('\r')
    return

def send_cmd(args):
    app = args[0].getApp()
    cmd_list = []
    file = args[1]
    times = int(args[2])

    if not os.path.exists(file):
        return False

    f = open(file, "r")
    while True:
        line = f.readline()
        if not line:
            f.close()
            break
        cmd_list.append(line)

    com_inst=app.PuTTY
    com_inst.type_keys('\r')

    for i in range(times):
        for cmd in cmd_list:
            com_inst.type_keys(cmd)
            com_inst.type_keys('\r')
            time.sleep(1)



def autoPutty(*args):
    parseropt = args[0]
    com = parseropt.getCOMPort()
    file = parseropt.getcmdFile()
    path = parseropt.getPath()
    times = parseropt.getTimes()
    pid = 0

    autoapp=Autoit(path)
    autoapp.open()
    pid = autoapp.getPID()

    if pid == 0:
        autoapp.Run(automate_putty, autoapp, com)
    else:
        autoapp.Run(send_cmd, autoapp, file, times)











