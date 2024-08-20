# -*-coding:utf-8-*-
import requests
import json
url = "https://coding-oj.gaotu100.com/api/get-user-home-info?uid=cc92409361844d5ca1d9f93778c45d55&username=郭梓朋"
h = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}
r = requests.get(url,headers=h)
print(r)
print(r.text)