try:
    from execute import *
except:
    from .execute import *
import os,sys

def demo():
    command = ""
    while command != "exit":
        command = input("Klam "+os.getcwd()+">")
        try:
            result = execute(command)
            print(result)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    demo()
