import sys

sys.path.extend([".\\gui", ".\\Klam", ".\\listenAndSay", ".\\myNL", ".\\spider"])

try:
    import Klam
    import myNL
    import listenAndSay
    import gui
except ImportError:
    from . import Klam
    from . import myNL
    from . import listenAndSay
    from . import gui
