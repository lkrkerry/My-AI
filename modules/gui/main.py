from tkinter import *
from tkinter import ttk
# Import tkinter and ttk

import sys
sys.path.append(".\\modules\\gui")    # let python know where gui files were.

import ke,fe,cal,shell,tdl,mainframe    # import the gui part file.

class UI:   # define the class UI
    def __init__(self):
        self.root = Tk() # Init the root
        self.fe = fe.fe(self.root, 0, 0) # File Explorer
        self.cal = cal.cal(self.root, 10, 0) # Calculater
        self.mf = mainframe.mf(self.root, 0, 10) # MainFrame
        self.shell = shell.shell(self.root, 10, 10) # Klam Shell
        self.ke = ke.ke(self.root, 0, 20) # Klam Editor
        self.tdl = tdl.tdl(self.root, 10, 20) # To Do List
    def start(self): # Start Function
        self.fe.start() # Start File Explorer
        self.cal.start() # Start Calculater
        self.mf.start() # Start MainFrame
        self.shell.start() # Start Klam Shell
        self.ke.start() # Start Klam Editor
        self.tdl.start() # Start To Do List
        mainloop() # Let TK know what I'm doing.

if __main__ == "__main__": # Check if main.py is been run by itself, not been imported.
    ui = UI() # Set ui into the UI class UI
    ui.start() # Start the ui
