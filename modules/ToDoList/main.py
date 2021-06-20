import time,sys,pickle
sys.path.append(".\\modules\\listenAndSay")
import lsa
from tkinter import ttk
from tkinter import *

def add():
    global ans_lst,todo,tm,mf,root
    ans_lst = {}
    answer = " "
    root = Tk()
    mf = ttk.Frame(root)
    mf.grid(column=0, row=0, sticky=(W,S,E,N))
    todo = StringVar()
    ttk.Entry(mf, textvariable=todo).grid(column=0,row=0)
    tm = StringVar()
    ttk.Label(mf, text="Example: "+time.strftime("%c")).grid(column=1,row=1)
    ttk.Entry(mf, textvariable=tm).grid(column=1,row=0)
    ttk.Button(mf, text="Add", command=ref).grid(column=2, row=0)
    a = ttk.Button(mf, text="Save", command=save).grid(column=3, row=0)
    ttk.Button(mf, text="Clear", command=save).grid(column=2, row=1)
    try:
        f = open(".\\tdl\\tdl.dat", 'rb')
        a = pickle.load(f)
    except:
        clear()
    ref()
    mainloop()

def clear():
    with open(".\\tdl\\tdl.dat", 'wb') as f:
        pass

def save():
    with open(".\\tdl\\tdl.dat", 'rb') as f:
        anl = pickle.load(f)
    anl.update(ans_lst)
    with open(".\\tdl\\tdl.dat", 'wb') as f:
        pickle.dump(anl, f)
    root.destroy()
    print(ans_lst)
    check()
    
def ref(*args):
    global a
    td = todo.get()
    ti = tm.get()
    ans_lst[ti] = td
    j = 0
    for i in ans_lst:
        ttk.Label(mf, text=ans_lst[i]).grid(column=0, row=j+3)
        ttk.Label(mf,text=i).grid(column=1,row=j+3)
        j += 1

def check():
    with open(".\\tdl\\tdl.dat", "rb") as f:
        tdl = pickle.load(f)
    count = 1
    while 1:
        if count == len(tdl):
            break
        current = time.strftime("%c")
        print(current)
        try:
            things = tdl[current]
        except:
            time.sleep(1)
        else:
            lsa.say_baidu("Master, It's "+current+"You should"+things)
            count += 1
    lsa.say_baidu("Bye Master.")

if __name__ == '__main__':
    tdl = add()
