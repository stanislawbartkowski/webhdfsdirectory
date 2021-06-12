""" Main program to launch proc/hdfs.py
"""
from proc.hdfs import HDFS
import logging

import sys
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def printhelp():
    print("Parameters: webhdfshost,webhdfsport,webhdfsuser, hdfsrootdir, hdfssuibdir,localdir,/dry run/, /regexp")
    print("")
    print("webhdfshost : WebHDFS hostname")
    print("webhdfsport : WebHDFS non-secure port number")
    print("webhdfsuser : HDFS user to authenticate")
    print("hdfsrootdir: HDFS start root dir")
    print("hdfssubdir: HDFS subdirectory of root dir")
    print("localdir : localdirectory to download")
    print("/dry run/ : optional, if 1 only browse HDFS directory structure without downloading")
    print("/dir reg exp/ : optional, regular expression to select a subset of HDFS directories to download")


def main():
    logging.info("Number: {0}  Args: {1} ".format(len(sys.argv), sys.argv))
    if len(sys.argv) <= 7:
        printhelp()
        sys.exit(4)
    WEBHDFSHOST = sys.argv[1]
    WEBHDFSPORT = sys.argv[2]
    WEBHDFSUSER = sys.argv[3]
    HDFSUSERDIR = sys.argv[4]
    HDFSDIR = sys.argv[5]
    LOCALDIR = sys.argv[6]
    DRYRUN = 0
    REGEXP = None
    if len(sys.argv) >= 8:
        DRYRUN = sys.argv[7]
    if len(sys.argv) >= 9:
        REGEXP = sys.argv[8]
    dryrun = DRYRUN == "1"
    if dryrun:
        logging.info("DRY RUN - browse HDFS tree only")
    H = HDFS(WEBHDFSHOST, WEBHDFSPORT, WEBHDFSUSER, REGEXP, dryrun)
    H.downloaddir(HDFSUSERDIR, HDFSDIR, LOCALDIR)


if __name__ == "__main__":
    # execute only if run as a script
    main()
