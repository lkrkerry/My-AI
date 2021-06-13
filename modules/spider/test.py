import requests

url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B6%AF%C2%FE%C5%AE%BA%A2%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000"

headers = {
    'User-Agent': 'Chrome/67.0.3396.62',
    'Host': 'www.baidu.com'
}

result = requests.get(url,headers=headers)
result.encoding = 'utf-8'
print(result.text)
