import os,time
from playsound import playsound
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '23924808'
API_KEY = 'kXEgbCG8VGcYf4FY17UOFMku'
SECRET_KEY = 'SEKW8d66X8eYgtMaK8VKhgfqzhir8bdR'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def say_baidu(sentence):
    result  = client.synthesis(sentence, 'zh', 1, {
        'vol': 5,
        'spd': 5,
        'per': 0,
    })
    if not isinstance(result, dict):
        t = time.time()
        with open('audio\\'+str(t)+'.mp3', 'wb') as f:
            f.write(result)
        playsound("audio\\"+str(t)+".mp3")
        return "success"
    else:
        return result

def say(sentence):
    audios = os.listdir(os.getcwd()+"..\\..\\audio")
    words = sentence.lower().split(" ")
    for word in words:
        try:
            playsound(".\\audio" + word + ".mp3")
            return "successfully played:"+word
        except:
            return "audio:"+word+" not found"

def listen():
    # try:
    #     os.system("del audio\listen.wav")
    # except:
    #     pass
    print(os.getcwd())
    os.system("cd audio;ffmpeg - i audio.mp3 - acodec pcm_s16le - ac 2 - ar 44100 listen.wav;cd ..")
    return client.asr(get_file_content('audio/listen.wav'), 'wav', 16000, {'dev_pid': 1537,})

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



if __name__ == "__main__":
    # print(say_baidu("I love you very much"))
    print(listen())
    print(say_baidu("hi"))
