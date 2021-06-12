# webhdfsdirectory

The application downloads HTTP directory recursively with subdirectories. It uses WebHDFS or HttpFS Rest/API interface. Current implementation is using only non-secure connection.

# Installation 

> git clone https://github.com/stanislawbartkowski/webhdfsdirectory.git

# Prereqs

* Python3
* requests: python3 -m pip install request3

# Configuration

> cd https://github.com/stanislawbartkowski/webhdfsdirectory.git<br>
> cp cp template/resource.rc .<br>
> vi resource.rc

| Variable | Description | Sample value
| ----- | ----- | ------ |
| WEBHDFSHOST | WebHDFS or HttpFS hostname | inimical1.fyre.ibm.com
| WEBHDFSPORT | Port number | 14000 for HttpFS or 9870 WebHDFS (Cloudera) or 50070 (HDP)
| WEBHDFSUSER | HDFS user accessing HDFS | Added as &user.name=WEBHDFSUSER to RestAPI URL
| LOGFILE | Log file path name | /tmp/hdfs/log.txt
| USERDIR | Root directory in HDFS. Directory to download is a subdirectory of USERDIR | /warehouse

# Usage 

> ./hdownload.sh hdfsdir localdir (optional)dryrun) (optional) regular expression to select directories for downloading

Parameters description<br>

| Parameter | Description | Sample value |
| -------- | ---------- | ----------- |
| hdfsdir | Subdirectory of USERDIR to download  | dir
| localdir | Local directory to store downloaded HDFS files | /tmp/download
| dryrun (optional) | equal 1 means that HDFS tree is walked through but no file is downloaded | 1
| regexp (optional) | regular expression used to select a subset of directory tree

# Example

HDFS tree<br>

* /user
* /user/sb/dir1
  * hello.txt
* /user/sb/dir1/dir11/
  * hello11.txt
* /user/sb/dir11
  * my11.txt
* /user//sb/dir2
  * hello2.txt




