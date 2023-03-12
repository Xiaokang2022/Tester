""" 图形界面 """
import tkinter
from tkinter import colorchooser, commondialog, scrolledtext, ttk

import tkintertools as tkt
from constants import *
from main import __version__

root = tkt.Tk('Python-v%s' % __version__, 1280, 720, 310, 150)


class Login:
    """ 登录界面 """

    canvas = tkt.Canvas(root, 1280, 720)
    tkt.CanvasLabel(canvas, 750, 120, 480, 370, 20, color_fill=('white',)*3)
    button_1 = tkt.CanvasButton(
        canvas, 770, 140, 160, 50, 10, '密码登录', font=('楷体', 20))
    button_2 = tkt.CanvasButton(
        canvas, 950, 140, 160, 50, 10, '验证码登录', font=('楷体', 20))
    entry_1 = tkt.CanvasEntry(
        canvas, 770, 210, 440, 50, 10, ('账号或邮箱号', '点击输入'), font=('楷体', 25), limit=20)
    entry_2 = tkt.CanvasEntry(
        canvas, 770, 280, 440, 50, 10, ('密码或验证码', '点击输入'), font=('楷体', 25), limit=16, show='•')
    tkt.CanvasButton(
        canvas, 770, 350, 440, 50, 10, '登  录', font=('楷体', 25), command=lambda: Login.login())
    tkt.CanvasButton(
        canvas, 770, 420, 130, 50, 10, '注册', font=('楷体', 25), command=lambda: Login.register())
    tkt.CanvasButton(
        canvas, 1050, 420, 160, 50, 10, '离线模式', font=('楷体', 25), command=lambda: Login.offline())
    canvas.create_text(
        990, 60, text='登录账号', font=('楷体', 35))
    canvas.create_text(
        990, 600, text=description, justify='center', font=('楷体', 15))
    face_image = tkt.PhotoImage('images/face/face1.png')
    canvas.create_image(340, 360, image=face_image)

    @classmethod
    def place(cls, flag: bool = True) -> None:
        """ 显示 """
        if flag:
            cls.canvas.place(x=0, y=0)
        else:
            cls.canvas.place_forget()

    @classmethod
    def register(cls) -> None:
        """ 注册 """

    @classmethod
    def login(cls) -> None:
        """ 登录 """

    @classmethod
    def offline(cls) -> None:
        """ 离线 """


class Home:
    """ 主页界面 """

    canvas = tkt.Canvas(root, 1280, 720)

    @classmethod
    def place(cls, flag: bool = True) -> None:
        """ 显示 """
        if flag:
            cls.canvas.place(x=0, y=0)
        else:
            cls.canvas.place_forget()


if __name__ == '__main__':
    from ctypes import OleDLL

    OleDLL('shcore').SetProcessDpiAwareness(1)
    Login.place()
    root.mainloop()
