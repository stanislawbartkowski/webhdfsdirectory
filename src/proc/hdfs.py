import json
import requests
import logging
import os
import re

""" Download HDFS directory tree using WebHDFS REST/API

  WebHDFS allows downloading a single file but there is no method to download the whole directory. This module adds this functionality.
  The module uses two WebHDSF Rest/API calls: 
     LISTSTATUS - to list the directory content
     OPEN - to download a file

  It supports only non-secure connection.
  There is an option to select only a specific directories for downloading through regular expression pattern.

  Typical usage:
    H = HDFS("hostname.ord.com",5670,webhdfsuser)
    H.downloaddir("/user/products","inventory","/home/products/landingzone")

  Error handling: in case of any error, en exception is thrown
    
"""

CHUNKSIZE = 64000


def bytesdownloaded(size):
    """ Reports number of bytes downloaded: as number of bytes and gigabytes.

    Args: 
      size: number of bytes

    Returns:
      information string
    """
    GB = round(size/1000000, 2)
    return "{0}B - {1}MB".format(str(size), str(GB))


class HDFS:

    """ Downloads wenHDFS directory

    Attributes:
       WEBHDFSHOST : WebHDFS hostname
       WEBHDFSPORT: WebHDFS port (non-secure)
       WEBHDFSUSER: HDFS user used to authenticated, example: hdfs
       DIRREG: Optional, regular expression used to select a subset of files to download.
               If not present - download all files
       dryrun: boolean, if true then browse only the directory tree and list files to download without downloading the content
               default: false, browse directory tree and download
    """

    def __init__(self, WEBHDFSHOST, WEBHDFSPORT, WEBHDFSUSER, DIRREG=None, dryrun=False):
        self.WEBHDFSHOST = WEBHDFSHOST
        self.WEBHDFSPORT = WEBHDFSPORT
        self.WEBHDFSUSER = WEBHDFSUSER
        self.DIRREG = DIRREG
        self.dryrun = dryrun

    """ List directory contend

    Args:
      dir: HDFS directory to list

    Returns:
      List of tuples (filename, True/False directory/file)
    """

    def getdir(self, dir):
        url = "http://{0}:{1}/webhdfs/v1{2}?op=LISTSTATUS&user.name={3}".format(
            self.WEBHDFSHOST, self.WEBHDFSPORT, dir, self.WEBHDFSUSER)
        logging.info("WebHDFS url: {0}".format(url))
        response = requests.get(url)
        if response.status_code == 200:
            js = json.loads(response.content.decode('utf-8'))
        else:
            raise Exception(
                dir + " list directory failed. Response code different than 200:" + str(response.status_code))
        files = js["FileStatuses"]["FileStatus"]
        list = []
        for f in files:
            name = f['pathSuffix']
            tf = f['type']
            list.append((name, tf == 'DIRECTORY'))

        return list

    def download(self, file, outfile):
        """ Deprecated """
        url = "http://{0}:{1}/webhdfs/v1{2}?op=OPEN&user.name={3}".format(
            self.WEBHDFSHOST, self.WEBHDFSPORT, file, self.WEBHDFSUSER)
        logging.info("Downloading:" + url)
        with requests.get(url) as response:
            if response.status_code == 200:
                f = response.content.decode('utf-8')
            else:
                raise Exception(
                    file + " download failed, response code different than 200:" + str(response.status_code))
            logging.info("Writing: " + outfile)
            with open(outfile, 'wb') as r:
                r.write(response.content)

    def downloadstream(self, file, outfile):
        """ Download a single HDFS file

        Args:
          file : HDFS file path name
          outfile: local file
        """
        url = "http://{0}:{1}/webhdfs/v1{2}?op=OPEN&user.name={3}".format(
            self.WEBHDFSHOST, self.WEBHDFSPORT, file, self.WEBHDFSUSER)
        logging.info("Downloading:" + url)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(outfile, 'wb') as f:
                size = 0
                no = 0
                for chunk in r.iter_content(chunk_size=CHUNKSIZE):
                    if chunk:
                        no = no + 1
                        size = size + len(chunk)
                        if no % 10 == 0:
                            logging.info(bytesdownloaded(size))
                        f.write(chunk)
                logging.info("Downloaded: {0}  {1}".format(
                    bytesdownloaded(size), outfile))

    def downloaddir(self, userdir, dir, outdir):
        """ Downloads HDFS directory tree

        Args:
          userdir: HDFS root directory
          dir: HDFS subdirectory in userdir to download
          oudir: local directory
        """
        d = os.path.join(userdir, dir)

        s = self.getdir(d)
        empty = True
        for e in s:
            (fname, isdir) = e
            empty = False

            if isdir:
                newd = os.path.join(dir, fname)
                if self.DIRREG != None:
                    if re.match(self.DIRREG, newd) == None:
                        logging.info(
                            "Directory {0} rejected by regexp {1}".format(newd, self.DIRREG))
                        continue
                    logging.info(
                        "Directory {0} matches regexp {1}".format(newd, self.DIRREG))
                self.downloaddir(userdir, newd, outdir)
                continue
            localpath = os.path.join(outdir, dir)
            if not os.path.isdir(localpath):
                os.makedirs(localpath)
            hdfsfile = os.path.join(userdir, dir, fname)
            localfile = os.path.join(localpath, fname)
            logging.info("DOWNLOADING FILE: {0} => {1}".format(hdfsfile, localfile))
            if not self.dryrun:
                self.downloadstream(hdfsfile, localfile)
        if empty:
            logging.info("HDFS {0} is empty, nothing to download".format(d))
