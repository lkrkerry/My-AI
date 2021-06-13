import os,sys
sys.path.append(os.path.join(os.getcwd(),"functions"))
sys.path.append(os.getcwd())
try:
    from executionFunctions import *
except:
    from .executionFunctions import *
import functions
class ExecutionNotFoundError(Exception):
    pass

def execute(command):
    words = command.split(" ")
    functions.log_in("Searching Klam Code: "+command)
    if words[0] in exec_dct:
        for key in exec_dct:
            if words[0] == key:
##                        print(words[1:])
                try:
                    a = words[1]
                except:
                    return exec_dct[key]([])
                else:
                    if a != "/?":
                        result = exec_dct[key](words[1:])
                        return result
                    else:
                        return exec_dct[key].__doc__
    else:
        functions.log_in("Command Not Found: "+command, "critical")
        raise ExecutionNotFoundError("Command:"+words[0]+" is not found.\nCheck your spelling and try it again.\n")

exec_dct = {
    "cd":cd,
    "pwd":pwd,
    "exit":myexit,
    "mkdir":mmkdir,
    "rmdir":mrmdir,
    "create-text-file":ct,
    "ctf":ct,
    "edit-text-file":et,
    "etf":et,
    "et":et,
    "ct":ct,
    "read-text-file":rf,
    "rtf":rf,
    "rf":rf,
    "rm":rm,
    "remove":rm,
    "remove-file":rm,
    "rf":rm,
    "rename":rn,
    "rename-f":rn,
    "rd":rn,
    "rename-d":rn,
    "ls":ls,
    "dir":ls,
    "list-str":ls,
    "trun":trun,
    "truncate":trun,
    }

if __name__ == "__main__":
    print(execute("pwd"))
