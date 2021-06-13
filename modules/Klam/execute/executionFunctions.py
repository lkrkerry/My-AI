import os,sys

class ExecutionError(Exception):
    pass

def cd(args):
    if args == []:
        return pwd([])
    else:
        try:
            os.chdir(args[0])
            return "Change Directory to "+args[0]+"\n"
        except:
            raise ExecutionError("Directory:"+args[0]+" not found.\n")

def pwd(args):
##      print(args)
    try:
        a = args[0]
    except:
        return os.getcwd()
    else:
        return "pwd don't need any thing.\n"
        

def myexit(args):
    if args != []:
        print("exit don't need any thing.\n")
    return "Exiting...\n"
    sys.exit(0)

def mmkdir(args):
    try:
        os.mkdir(args[0])
        return "Created "+args[0]+"\n"
    except:
        raise ExecutionError("Directory:"+args[0]+" can't be created\n")

def mrmdir(args):
    try:
        os.rmdir(args[0])
        return "Removed Directory "+args[0]+"\n"
    except:
        raise ExecutionError("Directory:"+args[0]+" cannot be removed\n")

def ct(args):
    try:
        f = open(args[0],'w')
        f.close()
        return "Successfully created text file:"+args[0]+"\n"
    except:
        raise ExecutionError("Text File:"+args[0]+" cannot be created.\n")

def et(args):
    try:
        mode = args[1]
    except IndexError:
        mode = 'w'
    else:
        mode = mode.lower()
        if (mode == '0') or (mode == 'w') or (mode == 'write'):
            mode = 'w'
        elif (mode == '1') or (mode == 'a') or (mode == 'append'):
            mode = 'a'
        else:
            raise ExecutionError("Mode should be 0,1 w or r\n")
        try:
            f = open(args[0],mode)
        except:
            raise ExceptionError("The textfile:"+args[0]+"cannot be opened\n")
        else:
            print("Opened text file:"+args[0]+"\n")
            try:
                result = f.write(args[2])
            except:
                raise ExecutionError("Cannot write:"+args[2]+" in textfile:"+args[0]+"\n")
            else:
                f.close()
                return "Written "+str(result)+" bytes in file:"+args[0]+"\n"

def rf(args):
    try:
        f = open(args[0],'r')
    except:
        raise ExecutionError("Cannot read textfile:"+args[0]+"\n")
    else:
        result = f.read()
        f.close()
        return result

def rm(args):
    try:
        os.remove(args[0])
    except:
        raise ExecutionError("Cannot remove file/directory:"+args[0]+"\n")
    else:
        return "Successfully removed "+args[0]+"\n"

def rn(args):
    try:
        os.rename(args[0],args[1])
    except:
        raise ExecutionError("Cannot rename file/directory:"+args[0]+" to:"+args[1]+"\n")
    else:
        return "Successfully renamed:"+args[0]+"to:"+args[1]

def ls(args):
    if args != []:
        print("ls don't need any thing.\n")
    try:
        return os.listdir(os.getcwd)
    except:
        raise ExecutionError("Cannot getall from:"+args[0])

def trun(args):
    try:
        os.truncate(args[0])
    except:
        raise ExecutionError("Cannot turncate file/directory :"+args[0])
    else:
        return "Successfully truncated "+args[0]
        
if __name__ == "__main__":
    myexit([])
