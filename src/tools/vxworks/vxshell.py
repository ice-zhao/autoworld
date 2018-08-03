
from awlib.autoit import *
from awlib.io import *

import subprocess
import time

class autoVxshell(object):
    def __init__(self, path):
        self.__path = path

    def send_cmd(self):
        pass

    def getPath(self):
        return self.__path



#-f "cmd.txt" -P "D:\DevelopmentTools\windriver\wrenv.exe -p vxworks-6.8"
def autoVxworkshell(*args):
    parseropt = args[0]
    path = parseropt.getPath()
    cmdfile = parseropt.getcmdFile()

    autoapp = Autoit(path)
    shell = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE)

    autoapp.parseCMDfile(cmdfile)

    for cmd in autoapp.cmd:
        shell.stdin.write(cmd)
        time.sleep(1)







