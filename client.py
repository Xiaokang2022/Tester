""" 客户端 """
import socket
import time
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
    def code(cls, mail: str) -> None:
        """ 验证码 """
        cls.send(op='CODE', mail=mail)


if __name__ == '__main__':
    Client.connect()
    print(1)
    time.sleep(0.1)
    Client.code('392126563@qq.com')
    print(2)
    time.sleep(0.1)
    Client.close()
    print(3)
