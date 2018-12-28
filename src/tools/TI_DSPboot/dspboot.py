import os
import sys
from pywinauto.application import Application
import shutil
import pyautogui
import time

from optparse import OptionParser

class ParserOptions(object):
    def __init__(self, options):
        for key, val in options.__dict__.items():
            setattr(self, key, val)

    def getInputFilesVal(self):
        return self.hvdsp

class TextArea(object):
    buffer = []
    def __init__(self):
        self.buffer = []
    def write(self, *args, **kwargs):
        self.buffer.append(args)
    def clear(self):
        self.buffer = []

if __name__ == "__main__":
    hvdsp = 'E:\PersionalDir\workspace_v5_5\C6746_220\Debug\C6746_220.out'

    parser=OptionParser(version="1.0.0",
    usage="""%prog -p path""")

    parser.add_option("-p","--path", help="specify the path of C6746_220 file",
                      action="store", dest="hvdsp",
                      default = 'E:\PersionalDir\workspace_v5_5\C6746_220\Debug\C6746_220.out')

    curr_path = os.path.realpath(os.path.curdir)
    outfile = "C6746_220.out"
#    app = Application(backend="uia").start("notepad.exe")
#    dlg_spec = app.window(title='Untitled - Notepad')
    app = Application(backend="uia").start("DSPBoot.exe")
    dspboot = app.DSPBootAssistTool
    outfile = curr_path + "\\" + outfile
    outfile_h = curr_path + "\\" + "C6746_220.h"
    destfile = curr_path + "\\" + "HPI_BootTable.h"

    options, args = parser.parse_args(sys.argv)
    parseropt=ParserOptions(options)

    hvdsp = parseropt.getInputFilesVal()
#    print hvdsp
    if os.path.exists(outfile_h):
        os.remove(outfile_h)
    if os.path.exists(outfile):
        os.remove(outfile)

    #copy "C6746_220.out" from HV project dir.
    shutil.copy(hvdsp, outfile)
#    print outfile
#    dspboot.Edit3.type_keys(outfile)
#    print outfile
    dspboot.Button6.click()        #click  'Open' button
    dlg_open = app.OpenTIDSP
    dlg_open.edit3.type_keys(outfile)        #File name editor, input file name
#    dlg_open.OpenButton.click()        #combox open button
    dlg_open.Button16.click()        #click Open button for opening file.

    #set options
    dspboot.Button1.click()    #click Option... button.
#    dlg_option = app.Window_(best_match=u'Options')
    dlg_option = app.Options
    #select .bss
    stdout = sys.stdout
    sys.stdout = TextArea()  #allocated memory area
    dlg_option.ListBox3.print_control_identifiers()
    winspec = sys.stdout
    dsp_sections = [".bss", ".const", ".data"]
#    print winspec.buffer
    left_offset = 5; right_offset = 0;
#    for tup in winspec.buffer:
    for sect in dsp_sections:
        locate = []  #save coordinate of listitems for .bss;.const;.data sections
        for tup in winspec.buffer:
            if tup[0].find(sect) > -1:
                grid = tup[0][tup[0].find('(')+1:tup[0].find(')')].split(',')
                for gridi in grid:
                    gridj = gridi.strip()
                    gridk = int(gridj[1:])
                    locate.append(gridk)
                pyautogui.moveTo(locate[0]+left_offset, locate[1]+right_offset)
                pyautogui.click(button='right')
                dlg_option.Button6.click()        #add to left listbox from middle listbox.
                break;
#        time.sleep(1)
        del sys.stdout
        sys.stdout = TextArea()
        dlg_option.ListBox3.print_control_identifiers()
        winspec = sys.stdout

    sys.stdout = stdout    #restore original stdout.

#    list_box3 = dlg_option.Pane2.ListBox3
    list_box3 = dlg_option['ListBox3']
    dlg_option.Pane1.checkbox2.click()        #select Swap Raw Data
    dlg_option.Pane1.checkbox3.click()        #select Swap Infomation (Address and Size)

#    print dlg_option.Pane2.listbox3.texts()
#    print dlg_option.Pane2.listbox3.item_count()
#    dlg_option.Pane2.listbox3.select(20)
#    list_box2 = dlg_option.Pane2.ListBox2
#    print list_box3.item_count()

    dlg_option.OKButton.click()

    #save this to file
    dspboot.Savetothisfile2.click()
    #exit
    dspboot.OK.OK.click()
    dspboot.close()

    #rename C6746_220.h to HPI_BootTable.h
    if os.path.exists(destfile):
        os.remove(destfile)
#    os.rename(outfile_h, destfile)
    if os.path.exists(outfile_h):
        fd = open(outfile_h, "rb")
        fw = open(destfile, "wb+")
        if fd is not None:
            while True:
                line = fd.readline()
                line = line.replace('C6746_220BootTable[]', 'HPI_BootTable[]')
                fw.write(line)
                if not line:
                    break
#        fd.write(fd.read().replace('C6746_220BootTable[]', 'HPI_BootTable[]')
#    os.remove(destfile)
#    open_file.write(newText)
#    list_box3.TypeKeys("{HOME}{DOWN 2}{ENTER}")
#    listbox.print_control_identifiers()
#    dlg_option.print_control_identifiers()
#    print dlg_open.ComboBox3.item_count()
#    print dlg_open.ComboBox1.texts()
#    dlg_open.print_control_identifiers()
#    dlg_open = app.window(best_math="OpenTIDSP")
#    dspboot.Button6.click()        #click Open button.
#    dspboot.Button0.click()        #click Options... button.
#    app.DSPBootAssistTool.draw_outline()
#    app.DSPBootAssistTool.print_control_identifiers()
#    dlg_spec = app.window(title='*DSP Boot Assist ToolV1.1*')
#    dlg_spec.wrapper_object()
#    print dlg_spec
#    app.UntitledNotepad.type_keys("%FX")
#    while(1):
#        pass