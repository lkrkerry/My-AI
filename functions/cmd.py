import os

def cmding(ins):
    que = ""
    while que != "quit":
        que = input(ins)
        rep = os.popen(que)
        print(rep.read())
#         print(dir(rep))
    print("Back to normal.")
    return "normal"
        
if __name__ == "__main__":
    cmding("cmd>")