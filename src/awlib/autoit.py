from pywinauto.application import Application
import shutil
import pyautogui
import time
import psutil
import os
import sys

class Autoit(object):
    #path: program path
    def __init__(self, path):
        self.__path = path
        self.__app = Application(backend="uia")
        self.__pid = 0
        self.exe_file = []
        self.__conn = False


    def open(self, title_str=None):
        #ensure one App instance when conn param is True
        if not os.path.exists(self.__path) or \
           not os.access(self.__path, os.X_OK):
            return False

#       connection is prefer.
        if title_str is not None:
            self.__app = Application.connect(self.__app, title=title_str)
        else:
            self.__app = self.__app.start(self.__path)

        #FIXME: to check __app is valid.
        self.__conn = True

    def findPID(self):
        pid = 0
        self.exe_file = []
        basename = os.path.basename(self.__path)
        for p in psutil.process_iter():
            pinfo = p.as_dict(attrs=['pid', 'name', 'username'])
            name=pinfo['name']
            if name == basename:
                pid=pinfo['pid']
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











