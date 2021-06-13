import sys,os

sys.path.append(os.getcwd())

try:
    from .robots import *
    from .calculate import *
    from .Database import *
    from .learn import *
    from .talk_function import *
    from .talk_sth import *
    from .trans import *
    from .log import *
##    from .klam import *
except ImportError:
    from robots import *
    from calculate import *
    from Database import *
    from learn import *
    from talk_function import *
    from talk_sth import *
    from trans import *
    from log import *
##    from klam import *

