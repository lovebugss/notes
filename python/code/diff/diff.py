"""文本对比工具
目前支持 并集, 差集, 交集

Usage:
  diff.py <file1> <file2> [-t <type>] [-o <output>]


Options:
    filename:   文件名
    -t      :   类型 ins uni dif
"""

from docopt import docopt
from difflib import Differ,HtmlDiff
import sys, difflib


def read(path):
    with open(path, 'r') as f:
        return f.readlines()


def main(file1, file2):
    d1 = read(file1)
    d2 = read(file2)
    differ = Differ()
    d = differ.compare(d1, d2)
    hd = HtmlDiff().make_file()
    sys.stdout.writelines(d)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')
    main(arguments['<file1>'], arguments['<file2>'])
