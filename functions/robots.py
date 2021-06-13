import time,sys,os

try:
    from .log import *
    from .talk_function import *
    from .calculate import *
    from .cmd import *
    import modules
    sys.path.extend([r"./functions",r"./modules",r"./modules/myNL",r"./modules/Klam"])
except ImportError:
    from talk_function import *
    from calculate import *
    from cmd import *
    from log import *
    sys.path.extend([r".",r"../../modules"])
    import modules
    
class AI():
    def __init__(self,name="Kristina",time=time.strftime("%c"),mode="normal",con=1,ins="normal>"):
        self.name = name
        self.time = time
        self.con = con
        self.ins = ins
        self.mode = mode
    
    def _trans_time(self,day):
        lst_week = [
            "Sunday",
            "Monday",
            "Tueday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
                    ]
        return lst_week[day]
    
    def start(self):
        while self.con:
            if self.mode == "normal":
                self.ins = "normal>"
                self.time = time.strftime("%Y %m %d, %H:%M:%S on ") + self._trans_time(int(time.strftime("%w")))
                result = input(self.ins)
                result = check(result,name=self.name,time=self.time)
                if result == "quit":
                    for l in logs:
                        l.logger.info("Quiting...")
                    self.con = 0
                elif result == "cal":
                    for l in logs:
                        l.logger.info("Entering Calculating Mode...")
                    self.mode = "calculate"
                    result = "calq"
                    self.ins = "calculate>"
                elif result == "cmd":
                    for l in logs:
                        l.logger.info("Entering CMD Mode...")
                    self.mode = "cmd"
                    self.ins = "cmd>"
                elif result == "klam":
                    for l in logs:
                        l.logger.info("Entering Klam Execution Mode...")
                    self.mode = "klam"
                    self.ins = ""
                else:
                    if bool(result):
                        log_in("Read: "+result)
                    modules.listenAndSay.say_baidu(result)
                    print(result)
#                 print(decode(result, self.name, self.time))
            elif self.mode == "calculate":
                log_in("Entered Calculating Mode", "info")
                self.mode = calculate(self.ins)
            elif self.mode == "cmd":
                log_in("Entered CMD Mode", "info")
                self.mode = cmding(self.ins)
            elif self.mode == "klam":
                log_in("Entered Klam Execute Mode", "info")
                modules.Klam.demo()
                self.mode = "normal"
def log_in(res, level="info"):
    for l in logs:
        if level == "debug":
            l.logger.debug(res)
        elif level == "info":
            l.logger.info(res)
        elif level == "warning":
            l.logger.warning(res)
        elif level == "error":
            l.logger.warning(res)
        else:
            l.logger.critical(res)


if "function" in os.getcwd():
    for l in logs:
        l.log.warning(
            "You should run with main, not robot.py. Something might be broken.")
os.chdir("audio")
for m in os.listdir():
    os.remove(m)
os.chdir("..")
os.chdir("logs")
for m in os.listdir():
    os.remove(m)
os.chdir("..")

logs = []
debug = Logger(".\\logs\\debug.log", level="debug")
info = Logger(".\\logs\\info.log")
error = Logger(".\\logs\\error.log", level="error")
logs.extend([debug, info, error])

if __name__ == "__main__":
    Kristina = AI(name="Kristina")
    Kristina.start()
    
