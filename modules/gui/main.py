from tkinter import *
from tkinter import ttk
# Import tkinter and ttk.

root = Tk()
root.title("Kristina")

fe = ttk.Frame(root, padding="3 3 12 12")
fe.grid(column=0, row=0, sticky=(W,))
shell = ttk.Frame(root, padding="3 3 12 12")
shell.grid(column=0, row=2, sticky=(S,))
cal = ttk.Frame(root, padding="3 3 12 12")
cal.grid(column=0, row=1, sticky=(W,))
ke = ttk.Frame(root, padding="3 3 12 12")
ke.grid(column=2, row=0, sticky=(N,E))
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=1, row=0, sticky=(N,))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

res = StringVar()
shell_ke = ttk.Label(shell, textvariable=res)
shell_ke.grid(column=0, row=0, sticky=(N,W,E))
com = StringVar()
shell_com = ttk.Entry(shell, textvariable=com, width=100)
shell_com.grid(column=0, row=1, sticky=(S,W))

root.mainloop()
