""" Main program to launch proc/hdfs.py
"""
import argparse
import logging
from pars import addargs

import sys
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

from proc.hdfs import DIRHDFS


def gettestargs(parser) :
    i = "/home/sbartkowski/work/webhdfsdirectory/testdata/inputhdfs.txt"

    return parser.parse_args([i,"inimical1","14000","sb","/user/sb","dir1","/tmp/download","--dryrun"])

def getargs(parser) :
    return parser.parse_args(sys.argv[1:])

def readargs():
    parser = argparse.ArgumentParser(
        description='Download HDFS using WEB REST/API')
    addargs(parser)

#    return gettestargs(parser)
    return getargs(parser)

def main():
    args =  readargs()
    T = DIRHDFS(args.host[0], args.port[0], args.user[0],args.regexp,args.dryrun)
    T.downloadhdfsdir(args.userdir[0], args.usersubdir[0], args.localdir[0])

if __name__ == "__main__":
    # execute only if run as a script
    main()
