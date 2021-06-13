import random

try:
    from .trans import *
    from .Database import *
except ImportError:
    from trans import *
    from Database import *

def learn(ch_str_raw, *args):
    if bool(args):
        for c in args:
            learn(c)
    ch_str = ch_str_raw.lower()
    if ch_str[:11] == "do you know":
        if ch_str[12:16] == "that":
            ch_lst = ch_str[17:].split(" ")
        else:
            ch_lst = ch_str[12:].split(" ")
        ch_lst = coding(ch_lst)
#         print(ch_lst)
        que = ch_lst[0]
        ans = " ".join(ch_lst[1:])
        print(d_upload(que, ans))
    else:
        try:
            res = download(ch_str)
        except:
            res = "no"
        return res
    
def download(question="*"):
    que_lst = question.split(" ")
    question = " ".join(coding(que_lst))
    ch_l = d_read(question)
    ch_ls = coding(ch_l)
#     print(ch_ls)
    return " ".join(list(random.choice(ch_ls))).capitalize()
    
def coding(ch_lst):
    for i in range(len(ch_lst)):
        if ch_lst[i] in tran:
            ch_lst[i] = tran[ch_lst[i]]
        else:
            continue
    return ch_lst

if __name__ == "__main__":
    learn("Do you know that you're my AI ?",
          "Do you know that I'm your master ?",
          "Do you know that 10*10 =100 ?",
          "Do you know that 10+10 =20 ?",
          "Do you know that 2+2 =4 ?",)
    print(download("you're"))
    d_close()
