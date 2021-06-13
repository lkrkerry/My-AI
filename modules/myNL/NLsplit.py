import sys,os
try:
    from .NLconf import *
except ImportError:
    from NLconf import *
sys.path.append(os.path.join(os.getcwd(), "functions"))
sys.path.append(os.getcwd())
import functions


class Sentence():
    def __init__(self, value):
        self.value = my_lower(value)
    def __str__(self):
        return self.decode()
    def decode(self):
        res = []
        ch = self.value + " "
        for cc in cc_lst:
            if cc in ch:
                ch_l = ch.split(cc)
                ch_ls = "\n".join(ch_l)
        ch_ls = my_lower(ch_ls)
        for shorting in shortings:
            sentl = ch_ls.split(shorting)
            ch_ls = shortings[shorting].join(sentl)
        for sent in ch_ls.split("\n"):
            sente = sent.split(" ")
            sente[0] = sente[0].capitalize()
            res.append(" ".join(sente))
        return "\n".join(res)

    def sentence_split(self):
        ch = self.value + " "
        for cc in cc_lst:
            if cc in ch:
                ch_l = ch.split(cc)
                ch_ls = "\n".join(ch_l)
        return ch_ls

    def word_split(self):
        decoded = self.__str__()
        decoded = " \n ".join(decoded.split("\n"))
        decoded = decoded.split(" ")
        return decoded

    def back(self):
        res = []
        words = self.word_split()
        while "\n" in words:
            words.remove("\n")
        for word in words:
            if word[-1:] == "d" or word[-1:] == "s":
                res.append(word[:-1])
            elif word[-2:] == "ly":
                res.append(word[:-2])
            elif word[-3:] == "ing":
                res.append(word[:-3])
            else:
                res.append(word)
        return change(" ".join(res))

    def label(self):
        res = {}
        splited = self.word_split()
#         print(splited)
        sentenc = my_lower(" ".join(splited))
#         print(sentenc)
#         print(self.back())
        for n in word_dct: #get the type
            for k in word_dct[n]: #get words of that type
                if k in sentenc: #check if the word in the sentence
#                     print(k,n)
                    try:
                        a = res[k]
                    except KeyError:
                        res[k] = (n,) #set result
                    else:
                        # print('a',a)
                        b = list(a)
                        # print("b",b)
                        b.append(n)
                        c = list(b)
                        # print("c",c)
                        res[k] = c
#         print(res)
##        print(res)
        return my_sort(res,splited)
    def get_zwb(self):
        idc = '0'
        ri = 0
        level = {"z":0,"w":0,"b":0,"d":0,"g":0,"u":0}
        result = {}
        spec = []
        labeled = self.label()
##        get zhu
        while level["z"] == 0:
            
            for i in range(len(labeled)):
##            print(labeled[i][1][0])
                if labeled[i][1][0] == 'np' or labeled[i][1][0] == 'name':
                    idc += '1'
                    result = select_zwb_dct("z",result,labeled[i])
##                    print(idc)
                    if labeled[i+1][1] == 'conj':
                        break
                elif labeled[i][1][0] == 'ap':
                    idc += '2'
##                    print(idc)
                    if labeled[i+1][1][0] == 'noun' or labeled[i+1][1][0] == 'name':
                        pass
##                        print(labeled[i+1])
                        # print(labeled)
##                        result = select_zwb_dct("z",result,labeled[i+1])
    ##                    print(result)
            level["z"] = 1
        return result
####                return result
##                    return result


def my_lower(str):
    try:
        assert type(str) == type('')
    except AssertionError:
        raise ValueError("my_lower's str should be str.")
    str_lst = str.lower()
    for spec in specialtilize_lst:
        stl = str_lst.split(spec)
        str_lst = specialtilize_lst[spec].join(stl)
    return str_lst

def change(sent):
    try:
        assert type(sent) == type('')
    except AssertionError:
        raise ValueError("change's sent should be str.")
    for spec in specialtilize_lst:
        sen = sent.split(spec)
        sent = specialtilize_lst[spec].join(sen)
    return sent

def my_sort(dct, sentence_lst):
    errors = []
    result = []
    lowered = my_lower(" ".join(sentence_lst))
    sentence_lst = lowered.split(" ")
    while "\n" in sentence_lst:
        sentence_lst.remove("\n")
    for word in sentence_lst:
        try:
            result.append(list((word,dct[word])))
        except KeyError:
            result.append((word,["unknown",]))
            errors.append(word)
#             print(result)
    if errors != [''] and bool(errors):
        print(errors)
##    print(result)
    return result

def select_zwb_dct(zwb,result,word_tuple):
##    print(word_tuple)
    try:
        result[zwb]
    except KeyError:
        result[zwb] = [word_tuple[0],]
    else:
        result[zwb].append(word_tuple[0])
    return result

def add_all(str):
    result = 0
    try:
        res = int(str)
    except:
        raise ValueError("'str' must be able to transinto int")
    else:
        for i in list(str):
            result += int(i)
        return result

if __name__ == "__main__":
    sentence = Sentence("Last Sunday, my father and I went to the park.")
#     print(sentence.word_split())
##    print(sentence.label())
    print(sentence.get_zwb())
    print(sentence)
