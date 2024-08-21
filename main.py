# # # -*-coding:utf-8-*-
# import requests
# url1 = "https://coding-oj.gaotu100.com/api/change-userInfo"
# h1 = {
#         "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
#         # "cookie":"JSESSIONID={}".format(c)
#         "cookie":"JSESSIONID=BD6181875E1E68B41FAE77005EA02F14"
# }
# d = {"username":"李俣嘉",
#      "gender":"secrecy",
#      "nickname":"Voldemort Cyborg Bit",
#      "signature":"<html>\n\n<head>\n    <meta charset = \"UTF-8\">\n    <title>个性简介</title>\n</head>\n\n<body>\n<i><h1><center>个性简介</center></h1></i>\n<strong><p>My name is Voldemort·Cyborg·Bit.</p>\n</strong>\n<img src = \"https://coding-oj.gaotu100.com/api/public/img/dd714f5a21114f03ad8448b7f100ea16.png\">\n<h3>变化</h3>\n<p>由于高途OJ对于HTML的限制太多了（不让运行JS，不让使用CSS）</p>\n<strong>所以</strong>\n<strong><a href=\"https://example.com\" target=\"_blank\">这是我的新主页（暂无）</a></strong>\n<p>最近稍微有点忙……（这个链接以后再更）</p>\n<br>\n<br>\n<br>\n<br>\n<strong>2024年7月19日10:50:53　有感而发</strong>\n<strong><center>丑奴儿·书博山道中壁　<sub>辛弃疾</sub></center></strong>\n<center>\n　　少年不识愁滋味，爱上层楼。爱上层楼，为赋新词强说愁。而今识尽愁滋味，欲说还休。欲说还休，却道“天凉好个秋”。\n</center>\n<br>\n<br>\n<br>\n<strong>2024年7月29日16:11:07　又有感而发</strong>\n<strong><center>无题　<sub>李隐</sub></center></strong>\n<center>\n相见时难别亦难，东风无力百花残。\n<br>\n春蚕到死丝方尽，蜡炬成灰泪始干。\n<br>\n晓镜但愁云鬓改，夜吟应觉月光寒。\n<br>\n蓬山此去无多路，青鸟殷勤为探看。\n</center>\n<br>\n<br>\n<br>\n<strong>2024年7月31日16:50:51　双有感而发</strong>\n<center>\n那么多数字，我只喜欢素数。那么多古诗，我只喜欢《酬乐天扬州初逢席上见赠》\n<br>\n那么多文言文，我只喜欢《岳阳楼记》和《醉翁亭记》。那么多单词，我只喜欢oil，paper，fly\n<br>\n那么多元素，我只喜欢钠。那么多物理定律，我只喜欢伯努利的发现\n</center>\n<br>\n<br>\n<br>\n<strong>2024年8月20日15:21:59　叒有感而发</strong>\n<center>\n恶魔：为什么他们都叫我恶魔？\n<br>\n天使：因为你杀人了。\n<br>\n恶魔：可是我分明是在救人！\n<br>\n天使：因为他们没有看见。\n<br>\n恶魔：为什么他们叫你天使？\n<br>\n天使：因为我救人了。\n<br>\n恶魔：可是明明是你杀的人！\n<br>\n天使：因为他们没有看见。。。。。。。\n<br>\n天使：你！你！你！。。。你这个恶魔！！！\n<br>\n恶魔：是啊，因为现在我觉得，其实做恶魔也没什么不好～你说是吧？“天使”\n</center>\n</body>\n\n</html>",
#      "school":"Tsinghua University",
#      "github":"https://github.com/Voldemort230102"}
# r1 = requests.post(url1,headers=h1,json=d)
# print(r1)
# print(r1.text)
import pyglet.font
from tkinter import Tk,Label
from tkinter.font import Font

import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    print("程序以管理员权限运行")
else:
    print("程序未以管理员权限运行")

root = Tk()
width = 900
height = 600
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry('{}x{}+{}+{}'.format(width, height, int(window_width/2-width/2), int(window_height/2-height/2)))
root.title('GTOJ API')
root.resizable(False, False)
root.iconbitmap('./icon/icon2128.ico')

custom_font = Font(family='华文隶书', size=12)
gtoj = Label(root, text='GTOJ API', font=(custom_font, 12))
gtoj.pack()

root.mainloop()