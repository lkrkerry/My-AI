import random
try:
    from .talk_sth import *
    from .learn import *
except ImportError:
    from talk_sth import *
    from learn import *

def check(ch_sth_raw,**kargs):
#     print(kargs)
    ch_str = ch_sth_raw.lower()
    res = learn(ch_str)
#     print(res)
    if res != "no":
        return res
    else:
        res = ""
        ch_lst = ch_str.split(" ")
        for word in ch_lst:
            for key in things_to_talk:
                key1 = key.split(",")
                for keyword in key1:
                    if keyword in word:
                        res = key
                        return decode(res,kargs)
                    else:
                        if key in ch_str:
                            res = key
                            return decode(res,kargs)
            else:
                return decode("cant",kargs)

def decode(ch,kargs):
    if ch in sp_lst:
        keys = things_to_talk[ch]
        res = random.choice(keys).format(**kargs)
        print(res)
        return ch
    else:
        keys = things_to_talk[ch]
        res = random.choice(keys).format(**kargs)
        return res
    
if __name__ == "__main__":
    name = "knl"
    checked_global = check("99*99",name=name,time=11)
#     result = decode(checked_global,name,11)
    print(checked_global)
#     print(result)