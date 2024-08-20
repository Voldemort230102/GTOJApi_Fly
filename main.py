import requests
url = "https://coding-oj.gaotu100.com/api/file/upload-avatar"
r = requests.post(url, files={'image': open('./image/avatar.jpg', 'rb')})