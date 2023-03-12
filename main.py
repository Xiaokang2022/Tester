""" 启动文件 """


__version__ = '0.0.3'
__author__ = '小康2022<2951256653@qq.com>'


if __name__ == '__main__':
    from ctypes import OleDLL

    from GUI import root

    OleDLL('shcore').SetProcessDpiAwareness(1)
    root.mainloop()
