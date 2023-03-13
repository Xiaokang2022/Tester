""" 图形界面 """
import tkinter
from tkinter import colorchooser, commondialog, scrolledtext, ttk

import tkintertools as tkt
from constants import *
from main import __version__

root = tkt.Tk('Python-v%s' % __version__, 1280, 720, 310, 150)
root.minsize(1280, 720)


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
    canvas_widgets: list[tkt._BaseWidget] = []
    title = canvas.create_text(990, 60, font=('楷体', 40))
    canvas.create_text(
        990, 640, text=DESCRIPTION, justify='center', font=('楷体', 15))
    face_image = tkt.PhotoImage('images/face/face1.png')
    canvas.create_image(340, 360, image=face_image)

    @classmethod
    def login_page(cls) -> None:
        """ 登录界面 """
        cls.canvas.itemconfigure(cls.title, text='登 录')
        for widget in cls.canvas_widgets:
            widget.destroy()
        cls.canvas_widgets = [
            tkt.CanvasLabel(cls.canvas, 750, 120, 480, 370,
                            20, color_fill=('white',)*3),
            tkt.CanvasEntry(cls.canvas, 770, 210, 440, 50,
                            10, ('账号或邮箱', '点击输入'), limit=20),
            tkt.CanvasEntry(cls.canvas, 770, 280, 440, 50, 10,
                            ('密码或验证码', '点击输入'), limit=16, show='•'),
            tkt.CanvasButton(cls.canvas, 770, 140, 160, 50, 10, '密码登录'),
            tkt.CanvasButton(cls.canvas, 950, 140, 160, 50, 10, '验证码登录'),
            tkt.CanvasButton(cls.canvas, 770, 350, 440, 50, 10,
                             '登  录', command=cls.login),
            tkt.CanvasButton(cls.canvas, 770, 420, 130, 50, 10,
                             '注册', command=cls.register_page),
            tkt.CanvasButton(cls.canvas, 1050, 420, 160, 50, 10, '离线模式', command=cls.offline)]

    @classmethod
    def register_page(cls) -> None:
        """ 注册界面 """

        def switch() -> None:
            """ 开关 """
            if cls.canvas_widgets[8].value:
                cls.canvas_widgets[8].configure(text='')
            else:
                cls.canvas_widgets[8].configure(text='✓')

        cls.canvas.itemconfigure(cls.title, text='注 册')
        for widget in cls.canvas_widgets:
            widget.destroy()
        cls.canvas_widgets = [
            tkt.CanvasLabel(cls.canvas, 750, 120, 480, 440,
                            20, color_fill=('white',)*3),
            tkt.CanvasEntry(cls.canvas, 770, 140, 440, 50,
                            10, ('昵称', '点击输入'), limit=10),
            tkt.CanvasEntry(cls.canvas, 770, 210, 440, 50,
                            10, ('邮箱', '点击输入'), limit=20),
            tkt.CanvasEntry(cls.canvas, 770, 280, 250, 50,
                            10, ('验证码', '点击输入'), limit=6),
            tkt.CanvasEntry(cls.canvas, 770, 350, 440, 50, 10,
                            ('密码', '点击输入'), show='•', limit=16),
            tkt.CanvasButton(cls.canvas, 1040, 280, 170, 50, 10, '发送验证码'),
            tkt.CanvasButton(cls.canvas, 770, 420, 440, 50, 10, '注 册'),
            tkt.CanvasButton(cls.canvas, 1050, 490, 160, 50,
                             10, '返回登录', command=cls.login_page),
            tkt.CanvasButton(cls.canvas, 770, 500, 30, 30, 5, command=switch),
            tkt.CanvasButton(cls.canvas, 810, 500, 125, 30, 0, '遵循注册协议', justify='left', font=('楷体', 15),
                             color_outline=tkt.COLOR_NONE, color_fill=tkt.COLOR_NONE,
                             color_text=('black', 'orange', 'blue'), command=cls.toplevel)]

    @classmethod
    def toplevel(cls) -> None:
        """ 注册协议 """
        toplevel = tkinter.Toplevel(root)
        toplevel.title('注册协议')
        toplevel.geometry('720x500+590+290')
        toplevel.transient(root)
        toplevel.focus_set()
        canvas = tkinter.Canvas(toplevel, width=720, height=500)
        canvas.create_text(360, 50, text='Python习题测试软件\n注册协议',
                           font=('楷体', 24), justify='center')
        canvas.create_text(20, 100, text=CONTENT, anchor='nw', font=('楷体', 15))
        canvas.pack()

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
    Login.login_page()
    # Login.register_page()
    # Tool.place(0, 0)
    root.mainloop()
