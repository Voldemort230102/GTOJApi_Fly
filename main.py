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
from tkinter import Tk,Label,Menu,Button
from matplotlib.font_manager import findSystemFonts,FontProperties
from tkinter.messagebox import showinfo,showwarning

import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def no_admin():
    print("程序未以管理员权限运行")

def void():
    pass

def position(pos,win_length):
    return int(pos-win_length/2)

def get_jsessionid():
    global root
    import webbrowser
    import pyautogui
    import time
    url = "https://coding-oj.gaotu100.com/home"
    # 提示信息
    showinfo("提示","此操作将会打开浏览器")
    showwarning("警告","在操作过程中请勿移动鼠标或使用键盘")
    showinfo("提示","在调出“开发者模式”后\n选择菜单栏中的“网络”\n然后按下F5刷新")
    showinfo("提示","在其中的左上角“筛选器”中输入“home”\n然后选择“home”\n在“请求标头”中找到“Cookie”\n并复制其对应的值粘贴到下一个窗口中")
    # 打开浏览器
    webbrowser.open(url)  # 在默认浏览器中打开指定的URL
    time.sleep(2)
    pyautogui.hotkey('f12')
    # 创建询问窗口
    root.attributes('-disable', True)
    width = 900
    height = 600
    ask = Tk()
    win_width = ask.winfo_screenwidth()
    win_height = ask.winfo_screenheight()
    ask.geometry('{}x{}+{}+{}'.format(width, height, position(win_width/2,width), position(win_height/2,height)))
    ask.title('GTOJApi Fly')
    ask.resizable(False, False)
    ask.iconbitmap('./icon/icon2128.ico')
    def ask_close():
        root.attributes('-disable', False)
        ask.destroy()
    ask.protocol('WM_DELETE_WINDOW', ask_close)
    ask.mainloop()

# 是否含义某字体
def if_have_font(name):
    fonts = findSystemFonts(fontpaths=None, fontext='ttf')
    font_names = [FontProperties(fname=font).get_name() for font in fonts]
    font_names = sorted(set(font_names))
    for font_name in font_names:
        if font_name.lower() == name.lower():
            return True
    return False

def main():
    global root
    width = 900
    height = 600
    root = Tk()
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.geometry('{}x{}+{}+{}'.format(width, height, position(window_width/2,width), position(window_height/2,height)))
    root.title('GTOJApi Fly')
    root.resizable(False, False)
    root.iconbitmap('./icon/icon2128.ico')

    # 创建菜单栏
    menu = Menu(root)
    root.config(menu=menu)

    # 添加一个"关于"菜单
    about_menu = Menu(menu, tearoff=False)
    menu.add_cascade(label="关于", menu=about_menu)
    about_menu.add_command(label="使用方法", command=void)
    about_menu.add_command(label="检查更新", command=void)
    about_menu.add_separator()
    about_menu.add_command(label="关于我们", command=void)

    # GTOJApi Fly表签
    gtoj1 = Label(root, text='GTOJApi Fly', font=("华文隶书", 70, "bold"))
    gtoj1.place(x=0,y=0)
    gtoj1.update()
    gtoj1_width = gtoj1.winfo_width()
    gtoj1_height = gtoj1.winfo_height()
    gtoj1.place(x=position(width/2,gtoj1_width), y=position(100,gtoj1_height))

    # 创建按钮
    jsessionid = Button(root, text="登入", bd=10, width= 10, height=1, font=('华文行楷',25), command=lambda:get_jsessionid())
    jsessionid.place(x=0, y=0)
    jsessionid.update()
    jsessionid_width = jsessionid.winfo_width()
    jsessionid_height = jsessionid.winfo_height()
    jsessionid.place(x=position(300,jsessionid_width),y=position(350,jsessionid_height))

    root.mainloop()

if __name__ == '__main__':
    # if is_admin():
    main()
    # else:
    #     no_admin()