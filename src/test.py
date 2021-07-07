""" Main program to launch proc/hdfs.py
"""
from proc.hdfs import TRAVERSEHDFS, DIRHDFS, TRAVERSEFILE, FILEHDFS
import logging

import sys
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def test1():
    T = TRAVERSEHDFS("inimical1", 14000, "sb")
    l = T.getdir("/user/sb/dir1")
    for e in l:
        print(e)

 #   T.downloaddir("/user/sb","dir1","/tmp/dir")

#    T = DIRHDFS("inimical1", 14000, "sb")
#    l = T.getdir("/user/sb/")
#    for e in l:
#        print(e)
#    T.downloaddir("/user/sb", "dir1", "/tmp/landing")


def test2():
    i = "/home/sbartkowski/work/webhdfsdirectory/testdata/inputhdfs.txt"
    dir = "dir1"
    T = TRAVERSEFILE(i)
    l = T.getdir(dir)
    for e in l:
        print(e)

#    T = FILEHDFS(i, "inimical1", 14000, "sb")
#    l = T.getdir("/user/sb/")
#    for e in l:
#        print(e)
#    T.downloaddir("/user/sb", "dir1", "/tmp/landing")


if __name__ == "__main__":
    # execute only if run as a script
    #    test1()
    test2()
