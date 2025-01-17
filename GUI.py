""" 图形界面 """
import threading
import tkinter

import client
import tkintertools as tkt
from constants import *
from main import __version__

root = tkt.Tk('Questioner-v%s' % __version__, 1280, 720, 310, 150)
root.minsize(1280, 720)


class FlyWindow:
    """ 浮窗 """

    bg_light = tkt.PhotoImage('images/Python_light.png')
    bg_dark = tkt.PhotoImage('images/Python_dark.png')

    def __init__(self, canvas: tkt.Canvas, text: str) -> None:
        self.label = tkt.Label(
            canvas, -305, 10, 300, 120, 10, text=text, image=self.bg_light)
        self.run()

    def run(self, key: int = 1) -> None:
        tkt.move(root, self.label, 315*key *
                 self.label.master.rx, 0, 500, 'smooth')
        if key == -1:
            return self.label.master.after(500, self.label.destroy)
        self.label.master.after(3000, self.run, -1)


class Interface:
    """ 界面基类 """

    canvas: tkt.Canvas = None

    @classmethod
    def place(cls, x: int | None = None, y: int | None = None) -> None:
        """ 显示 """
        if flag := x != None:
            cls.canvas.place(
                x=x*cls.canvas.rx, y=y*cls.canvas.ry)
        else:
            cls.canvas.place_forget()
        cls.canvas.lock(flag)


class Login(Interface):
    """ 登录界面 """

    canvas = tkt.Canvas(root, 1280, 720, lock=False)
    canvas_widgets: list[tkt._BaseWidget] = []
    title = canvas.create_text(990, 60, font=('楷体', 40))
    canvas.create_image(990, 640, image=FlyWindow.bg_light)
    canvas.create_text(
        990, 640, text=DESCRIPTION, justify='center', font=('楷体', 16))
    face_image = tkt.PhotoImage('images/face/face1.png')
    canvas.create_image(340, 360, image=face_image)

    @classmethod
    def login_page_psd(cls) -> None:
        """ 登录界面 """
        cls.canvas.itemconfigure(cls.title, text='登 录')
        for widget in cls.canvas_widgets:
            widget.destroy()
        cls.canvas_widgets = [
            tkt.Label(cls.canvas, 750, 120, 480, 370,
                      20, color_fill=('white',)*3),
            tkt.Entry(cls.canvas, 770, 210, 440, 50,
                      10, ('邮箱', '点击输入'), limit=20),
            tkt.Entry(cls.canvas, 770, 280, 440, 50, 10,
                      ('密码', '点击输入'), limit=16, show='•'),
            tkt.Button(cls.canvas, 770, 140, 160, 50, 10,
                       '验证码登录', command=cls.login_page_code),
            tkt.Button(cls.canvas, 770, 350, 440, 50, 10,
                       '登  录', command=lambda: cls.login('PASSWORD')),
            tkt.Button(cls.canvas, 770, 420, 130, 50, 10,
                       '注册', command=cls.register_page),
            tkt.Button(cls.canvas, 1050, 420, 160, 50, 10, '离线模式', command=cls.offline)]

    @classmethod
    def login_page_code(cls) -> None:
        """ 登录界面 """
        cls.canvas.itemconfigure(cls.title, text='登 录')
        for widget in cls.canvas_widgets:
            widget.destroy()
        cls.canvas_widgets = [
            tkt.Label(cls.canvas, 750, 120, 480, 370,
                      20, color_fill=('white',)*3),
            tkt.Entry(cls.canvas, 770, 210, 440, 50,
                      10, ('邮箱', '点击输入'), limit=20),
            tkt.Entry(cls.canvas, 770, 280, 250, 50, 10,
                      ('验证码', '点击输入'), limit=16, show='•'),
            tkt.Button(cls.canvas, 1040, 280, 170, 50, 10, '获取验证码'),
            tkt.Button(cls.canvas, 770, 140, 160, 50, 10,
                       '密码登录', command=cls.login_page_psd),
            tkt.Button(cls.canvas, 770, 350, 440, 50, 10,
                       '登  录', command=lambda: cls.login('CODE')),
            tkt.Button(cls.canvas, 770, 420, 130, 50, 10,
                       '注册', command=cls.register_page),
            tkt.Button(cls.canvas, 1050, 420, 160, 50, 10, '离线模式', command=cls.offline)]

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
            tkt.Label(cls.canvas, 750, 120, 480, 440,
                      20, color_fill=('white',)*3),
            tkt.Entry(cls.canvas, 770, 140, 440, 50,
                      10, ('昵称', '点击输入'), limit=10),
            tkt.Entry(cls.canvas, 770, 210, 440, 50,
                      10, ('邮箱', '点击输入'), limit=20),
            tkt.Entry(cls.canvas, 770, 280, 250, 50,
                      10, ('验证码', '点击输入'), limit=6),
            tkt.Entry(cls.canvas, 770, 350, 440, 50, 10,
                      ('密码', '点击输入'), show='•', limit=16),
            tkt.Button(cls.canvas, 1040, 280, 170, 50, 10, '获取验证码',
                       command=lambda: cls.code(cls.canvas_widgets[2].value, 'REGISTER')),
            tkt.Button(cls.canvas, 770, 420, 440, 50,
                       10, '注 册', command=cls.register),
            tkt.Button(cls.canvas, 1050, 490, 160, 50,
                       10, '返回登录', command=cls.login_page_psd),
            tkt.Button(cls.canvas, 770, 500, 30, 30, 5, command=switch),
            tkt.Button(cls.canvas, 810, 500, 125, 30, 0, '同意注册协议', justify='left', font=('楷体', 15),
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
    def code(cls, mail: str, mode: str) -> None:
        """ 获取验证码 """
        if not mail:
            return FlyWindow(cls.canvas, '请填写邮箱')
        client.Client.code(mail, mode)

    @classmethod
    def register(cls) -> None:
        """ 注册 """
        if not cls.canvas_widgets[-2].value:
            return FlyWindow(cls.canvas, '请勾选注册协议')
        if not cls.canvas_widgets[1].value:
            return FlyWindow(cls.canvas, '请填写昵称')
        if not cls.canvas_widgets[2].value:
            return FlyWindow(cls.canvas, '请填写邮箱')
        if not cls.canvas_widgets[4].value:
            return FlyWindow(cls.canvas, '请填写密码')
        if not cls.canvas_widgets[3].value:
            return FlyWindow(cls.canvas, '请填写验证码')
        nickname = cls.canvas_widgets[1].value
        mail = cls.canvas_widgets[2].value
        code = cls.canvas_widgets[3].value
        password = cls.canvas_widgets[4].value
        client.Client.register(nickname, mail, code, password)

    @classmethod
    def login(cls, mode: str) -> None:
        """ 登录 """
        if not cls.canvas_widgets[1].value:
            return FlyWindow(cls.canvas, '请输入邮箱')
        if not cls.canvas_widgets[2].value:
            return FlyWindow(cls.canvas, '请输入密码' if mode == 'PASSWORD' else '请输入验证码')
        mail = cls.canvas_widgets[1].value
        password_or_code = cls.canvas_widgets[2].value
        client.Client.login(mode, mail, password_or_code)

    @classmethod
    def offline(cls) -> None:
        """ 离线 """
        return FlyWindow(cls.canvas, '离线模式正在开发中')


class Tool(Interface):
    """ 工具栏 """

    canvas = tkt.Canvas(root, 80, 720, lock=False, bg='white')
    tkt.Button(canvas, 10, 10, 60, 60, 8, '主页')
    tkt.Button(canvas, 10, 80, 60, 60, 8, '文件')
    tkt.Button(canvas, 10, 510, 60, 60, 8, '消息')
    tkt.Button(canvas, 10, 580, 60, 60, 8, '用户')
    tkt.Button(canvas, 10, 650, 60, 60, 8, '设置')


class Title(Interface):
    """ 标题栏 """

    canvas = tkt.Canvas(root, 1200, 720, lock=False)
    tkt.Button(canvas, 20, 20, 200, 50, 10, '邮件')
    tkt.Button(canvas, 240, 20, 200, 50, 10, '私信')


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


class Receiver:
    """ 接收器 """

    @classmethod
    def run(cls) -> None:
        """ 接收 """
        while True:
            data = client.Client.recv()
            match data['op']:
                case 'REGISTER':
                    if data['state'] == 'REGISTER_OK':
                        FlyWindow(Login.canvas, '— 注册成功 —')
                    elif data['state'] == 'REGISTER_REPEAT':
                        FlyWindow(Login.canvas, '邮箱重复注册')
                    elif data['state'] == 'REGISTER_ERROR':
                        FlyWindow(Login.canvas, '验证码错误')
                case 'LOGIN':
                    if data['state'] == 'LOGIN_OK':
                        FlyWindow(Login.canvas, '— 登录成功 —')
                    else:
                        if data['mode'] == 'PASSWORD':
                            FlyWindow(Login.canvas, '邮箱或密码不正确')
                        else:
                            FlyWindow(Login.canvas, '邮箱或验证码不正确')


def main() -> None:
    """ 主函数 """
    tkt.SetProcessDpiAwareness()
    Login.place(0, 0)
    Login.login_page_psd()
    # client.Client.connect()
    # threading.Thread(target=Receiver.run, daemon=True).start()
    root.mainloop()


if __name__ == '__main__':
    main()
