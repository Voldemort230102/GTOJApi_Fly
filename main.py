# # -*-coding:utf-8-*-
import requests
url = "https://coding-oj.gaotu100.com/api/login"
data = {
        "username":"李俣嘉",
        "password":"13936277872"
}
r = requests.post(url,json=data)
print(r.text)
c = r.cookies["JSESSIONID"]
print(c)


url1 = "https://coding-oj.gaotu100.com/api/get-user-home-info"
h1 = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "cookie":c
}
r1 = requests.get(url,headers=h1)
print(r1)
print(r1.text)