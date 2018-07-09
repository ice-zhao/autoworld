import os
import sys
from pywinauto.application import Application
import shutil
import psutil
from optparse import OptionParser

from putty.putty import *

class ParserOptions(object):
    def __init__(self, options):
        for key, val in options.__dict__.items():
            setattr(self, key, val)

    def getCOMPort(self):
        return self.com

    def getcmdFile(self):
        return self.file

    def getPath(self):
        return self.path

    def getTimes(self):
        return self.times

if __name__ == '__main__':
    parser=OptionParser(version="1.0.0",
    usage="""%prog -p path""")

    parser.add_option("-p","--port", help="specify COM port.",
                      action="store", dest="com", default = 'COM3')

    parser.add_option("-f","--cmd-file", help="command file.",
                      action="store", dest="file", default = '\r')

    parser.add_option("-P","--path", help="program to automate.",
                      action="store", dest="path", default = '')

    parser.add_option("-t","--times", help="execute command list until specific times.",
                      action="store", dest="times", default = 1)

    options, args = parser.parse_args(sys.argv)
    parseropt=ParserOptions(options)

    autoPutty(parseropt)











