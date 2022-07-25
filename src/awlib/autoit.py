import os

import psutil
from pywinauto.application import Application


class Autoit(object):
    # path: program path
    def __init__(self, path):
        self.__path = path
        self.__app = Application(backend="uia")
        self.__pid = 0
        self.exe_file = []
        self.__conn = False
        self.__bare_path = self.__path.split(' ')[0]
        self.cmd = []

    def open(self, title_str=None):
        # ensure one App instance when conn param is True
        if not os.path.exists(self.__bare_path) or \
                not os.access(self.__bare_path, os.X_OK):
            return False

        #       connection is prefer.
        if title_str is not None:
            self.__app = Application.connect(self.__app, title=title_str)
        else:
            self.__app = self.__app.start(self.__path)

        # FIXME: to check __app is valid.
        self.__conn = True

    def findPID(self):
        pid = 0
        self.exe_file = []
        bare_path = self.__path.split(' ')[0]
        basename = os.path.basename(bare_path)
        for p in psutil.process_iter():
            pinfo = p.as_dict(attrs=['pid', 'name', 'username'])
            name = pinfo['name']
            if name == basename:
                pid = pinfo['pid']
                self.exe_file.append(pinfo)
        #                print pinfo
        return pid

    def Run(self, Automation=None, *args):
        if Automation is not None:
            Automation(args)
        return

    def getApp(self):
        return self.__app

    def close(self):
        return True

    def getPID(self):
        return self.__pid

    def getPath(self):
        return self.__path

    def isConn(self):
        return self.__conn

    def Conn(self, pid):
        self.__app = Application.connect(self.__app, process=pid)
        return self.__app

    def parseCMDfile(self, file):
        self.cmd = []
        if not os.path.exists(file):
            return False

        f = open(file, "r")
        while True:
            line = f.readline()
            if not line:
                f.close()
                break
            if line.find('(') > 0:
                line = line.replace('(', '+9')
            if line.find(')') > 0:
                line = line.replace(')', '+0')
            self.cmd.append(line)
        return True

    def getControlInfo(self, control):
        return control.print_control_identifiers()
