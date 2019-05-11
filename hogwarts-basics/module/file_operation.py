import os
import sys


class FileOperation:

    def openfile(file_path):
        f_foo = open(file_path, "r")
        print(f_foo.read())
        f_foo.close()

    def openfile_utf8(file_path):
        f_foo = open(file_path, "r", encoding="utf8")
        print(f_foo.read())
        f_foo.close()

    if __name__ == '__main__':
        openfile("../../resouce/test.log")

