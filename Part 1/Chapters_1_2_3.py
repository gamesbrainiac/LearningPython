__author__ = 'Nafiul Islam'
__title__ = 'Chapters 1, 2 and 3'


import this
import os
import sys


def main(argv):
    if argv is None:
        argv = sys.argv

    print()
    print('OS path:', os.path)
    print('System version:' ,sys.version)

    print("Hello World", argv)


if __name__ == "__main__":
    main('Nafiul')

