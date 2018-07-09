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


    def open(self):
        #ensure one App instance when conn param is True
        if not os.path.exists(self.__path) or \
           not os.access(self.__path, os.X_OK):
            return False

        self.__pid = self.findPID()

        if self.__pid > 0:
            self.__app = Application.connect(self.__app,process=self.__pid)
        else:
            self.__app = self.__app.start(self.__path)

    def findPID(self):
        pid = 0
        basename = os.path.basename(self.__path)
        for p in psutil.process_iter():
            pinfo = p.as_dict(attrs=['pid', 'name', 'username'])
            name=pinfo['name']
            if name == basename:
                pid=pinfo['pid']
                break
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













