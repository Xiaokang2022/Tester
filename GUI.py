""" 图形界面 """
from tkinter import colorchooser, commondialog, scrolledtext, ttk

import tkintertools as tkt
from constants import *
from main import __version__

root = tkt.Tk('Python-v%s' % __version__, 1280, 720, 310, 150)


class Interface:
    """ 界面基类 """

    canvas: tkt.Canvas = None

    @classmethod
    def place(cls, x: int | None = None, y: int | None = None) -> None:
        """ 显示 """
        if flag := x != None:
            cls.canvas.place(
                x=x*cls.canvas.rate_x, y=y*cls.canvas.rate_y)
        else:
            cls.canvas.place_forget()
        cls.canvas.lock = flag


class Login(Interface):
    """ 登录界面 """

    canvas = tkt.Canvas(root, 1280, 720, lock=False)
    tkt.CanvasLabel(canvas, 750, 120, 480, 370, 20, color_fill=('white',)*3)
    button_1 = tkt.CanvasButton(
        canvas, 770, 140, 160, 50, 10, '密码登录', font=('楷体', 20))
    button_2 = tkt.CanvasButton(
        canvas, 950, 140, 160, 50, 10, '验证码登录', font=('楷体', 20))
    entry_1 = tkt.CanvasEntry(
        canvas, 770, 210, 440, 50, 10, ('账号或邮箱号', '点击输入'), limit=20)
    entry_2 = tkt.CanvasEntry(
        canvas, 770, 280, 440, 50, 10, ('密码或验证码', '点击输入'), limit=16, show='•')
    tkt.CanvasButton(
        canvas, 770, 350, 440, 50, 10, '登  录', command=lambda: Login.login())
    tkt.CanvasButton(
        canvas, 770, 420, 130, 50, 10, '注册', command=lambda: Login.register())
    tkt.CanvasButton(
        canvas, 1050, 420, 160, 50, 10, '离线模式', command=lambda: Login.offline())
    canvas.create_text(
        990, 60, text='登录账号', font=('楷体', 40))
    canvas.create_text(
        990, 640, text=DESCRIPTION, justify='center', font=('楷体', 15))
    face_image = tkt.PhotoImage('images/face/face1.png')
    canvas.create_image(340, 360, image=face_image)

    @classmethod
    def register(cls) -> None:
        """ 注册 """

    @classmethod
    def login(cls) -> None:
        """ 登录 """

    @classmethod
    def offline(cls) -> None:
        """ 离线 """


class Tool(Interface):
    """ 工具栏 """

    canvas = tkt.Canvas(root, 80, 720, lock=False, bg='white')
    tkt.CanvasButton(canvas, 10, 10, 60, 60, 8, '主页')
    tkt.CanvasButton(canvas, 10, 80, 60, 60, 8, '文件')
    tkt.CanvasButton(canvas, 10, 510, 60, 60, 8, '消息')
    tkt.CanvasButton(canvas, 10, 580, 60, 60, 8, '用户')
    tkt.CanvasButton(canvas, 10, 650, 60, 60, 8, '设置')


class Title(Interface):
    """ 标题栏 """

    canvas = tkt.Canvas(root, 1200, 720, lock=False)
    tkt.CanvasButton(canvas, 20, 20, 200, 50, 10, '邮件')
    tkt.CanvasButton(canvas, 240, 20, 200, 50, 10, '私信')


class State(Interface):
    """ 状态栏 """


class Home(Interface):
    """ 主页 """


class File(Interface):
    """ 文件 """


class Message(Interface):
    """ 邮箱 """


class User(Interface):
    """ 用户 """


class Config(Interface):
    """ 设置 """


if __name__ == '__main__':
    tkt.SetProcessDpiAwareness()
    Login.place(0, 0)
    # Tool.place(0, 0)
    root.mainloop()
