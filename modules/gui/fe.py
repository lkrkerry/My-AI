# Import tkinter module
from tkinter import *
from tkinter import ttk

import os # Import the module os



class fe: # define the part of the gui:fe
    def __init__(self, root, srow, scol): # set initions
        self.root = root
        self.srow = srow
        self.scol = scol
        self.pd = os.getcwd() # Get the current working directory
        self.cmls = {} # set a blank dict for commands
        self.ld = os.listdir(self.pd) # Get Children from self.pd
        for a in range(len(self.ld)):
            self.cmls[self.ld[a]] = lambda: os.chdir(self.ld[a])

    def start(self):
        bts = [] # set the list for buttons
        cur = 0
        for a in range(len(self.ld)):
            bt = ttk.Button(self.root, text=self.ld[a], command=self.cmls[self.ld[a]]) # Make the button named by the file
            bts.append(bt)
            bt.grid(column=self.scol, row=self.srow+cur)
            cur = cur + 1
    
    def ref(self):
        pass




if __name__ == "__main__":
    f = fe(Tk(), 0, 0)
    f.start()
    mainloop()
