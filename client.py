""" 客户端 """
import socket
from constants import *


class Client:
    """ 客户端 """

    client = socket.socket()

    @classmethod
    def connect(cls) -> None:
        """ 连接 """
        cls.client.connect((ADDRESS, PORT))
        cls.send(op='CLIENT')

    @classmethod
    def close(cls) -> None:
        """ 断开 """
        cls.send(op='QUIT')
        cls.client.close()

    @classmethod
    def send(cls, **kw) -> None:
        """ 发送 """
        return cls.client.send(kw.__repr__().encode())

    @classmethod
    def recv(cls) -> dict:
        """ 接受 """
        return eval(cls.client.recv(4096).decode())

    @classmethod
    def code(cls, mail: str, mode: str) -> None:
        """ 验证码 """
        cls.send(op='CODE', mode=mode, mail=mail)

    @classmethod
    def register(cls, nickname: str, mail: str, code: str, password: str) -> None:
        """ 注册 """
        cls.send(
            op='REGISTER', nickname=nickname, mail=mail, code=code.upper(), password=password)

    @classmethod
    def login(cls, mode: str, mail: str, password_or_code: str) -> None:
        """ 登录 """
        if mode == 'PASSWORD':
            cls.send(op='LOGIN', mode=mode, mail=mail,
                     password=password_or_code)
        else:
            cls.send(op='LOGIN', mode=mode, mail=mail, code=password_or_code)
