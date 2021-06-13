from talk_sth import *
from learn import *
import random

def decode(ch):
    keys = things_to_talk[ch]
    res = random.choice(keys)
    return res