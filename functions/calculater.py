import copy

class CalculationError(Exception):
    pass

class cal():
    def __init__(self, tens, mode="10", shortest_len=8, getdown=""):
        if getdown != "":
            tens -= 2**getdown
        self.tens = tens
        self.mode = mode
        self.getdown = getdown
        self.shortest_len = shortest_len
        self.binary = setlen(tens_into(self.tens), self.shortest_len)
        self.eights = setlen(tens_into(self.tens, 8), self.shortest_len)
        self.sixteens = setlen(tens_into(self.tens, 16), self.shortest_len)
        self.others = {"2":self.binary, "10":str(self.tens), "8":self.eights, "16":self.sixteens}
    def __str__(self):
        try:
            return self.others[self.mode]
        except KeyError:
            raise CalculationError("Value Not Found: "+self.mode)
    def __add__(self, other, getdown=""):
        result = []
        next = 0
        a = list(self.binary)
        b = list(other.binary)
        if a[0] != 0 or b[0] != 0:
            a.insert(0, "0")
            b.insert(0, "0")
        a = a[::-1]
        b = b[::-1]
        # print(a, b)
        for i,j in zip(a,b):
#             print(i, j)
            d,c = add_all(i,j,str(next))
#             print("d",d,c)
            next = c
            result.append(str(d))
#             print(result)
        res = "".join(result[::-1])
        answer = into_tens(res)
        return cal(answer, mode=self.mode, getdown=getdown)

def setlen(s, l):
    s = str(s)
    while len(s) < l:
        a = list(s)
        a.insert(0, "0")
        s = "".join(a)
    return s


def tens_into(tens, val=2):
    result = []
    present = copy.deepcopy(tens)
    while present != 0:
        result.append(str(present % val))
        present = present // val
    result = result[::-1]
    return "".join(result)

def into_tens(things, val=2):
    result = 0
    t = list(things)[::-1]
    for i in range(len(t)):
        current = 2**i
        if t[i] == "1":
            result += current
    return result

def add_all(a,b,c):
#     print(a,b,c)
    d1, c1 = add_half(a, b)
#     print("d1",d1, c1)
    d2, c2 = add_half(d1, c)
    # print("d2", d2,c2)
    return d2, bor(c1,c2)

def band(a,b):
    if a == "1":
        return b
    else:
        return "0"

def bxor(a,b):
    if a == b:
        return "0"
    else:
        return "1"

def bor(a,b):
    if a == "0":
        return b
    else:
        return "1"

def bnot(a):
    if a == "0":
        return "1"
    else:
        return "0"

def add_half(a,b):
    return bxor(a,b), band(a,b)

if __name__ == '__main__':
    a = cal(300)
    print(a.binary)
    b = cal(500)
    print(b.binary)
    print(b-a)
