import sqlite3

try:
    conn = sqlite3.connect(r"./database/lite.db")
except sqlite3.OperationalError:
    conn = sqlite3.connect(r"../database/lite.db")
cur = conn.cursor()

def d_upload(que,ans):
    com = 'insert into memory values ("{que}","{ans}")'.format(que=que,ans=ans)
#     print(com)
    cur.execute(com)
    return "I remembered: {0} {1}".format(que, ans)

def d_close():
    conn.commit()
    cur.close()
    conn.close()
    
def d_read(ques="*"):
    if ques == "*":
        cur.execute('select distinct questions,answers from memory')
        return cur.fetchall()
    else:
        ques = ques.lower()
        cur.execute('select distinct questions,answers from memory where questions="{}"'.format(ques))
        return cur.fetchall()

if __name__ == "__main__":
    print(d_read("3+3"))
    print(d_read())
    d_close()
