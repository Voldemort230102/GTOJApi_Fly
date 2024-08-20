# -*-coding:utf-8-*-
import requests
import json
url = "https://coding-oj.gaotu100.com/api/get-user-home-info?uid=c1d7f94044a2485ea89761d5332e1121"
h = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
r = requests.get(url,headers=h)
print(r)
print(r.text)
print(r.cookies)