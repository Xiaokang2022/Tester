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
        cls.send(code='CLIENT')

    @classmethod
    def close(cls) -> None:
        """ 断开 """
        cls.send(code='QUIT')
        cls.client.close()

    @classmethod
    def send(cls, **kw) -> None:
        """ 发送 """
        return cls.client.send(kw.__repr__().encode())

    @classmethod
    def recv(cls) -> dict:
        """ 接受 """
        return eval(cls.client.recv(4096).decode())


if __name__ == '__main__':
    Client.connect()
    time.sleep(0.1)
    Client.close()
