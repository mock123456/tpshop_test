"""
这个文件用于自定义异常类型
"""


class Error(Exception):
    def __str__(self):
        print('这是一个错误类')

