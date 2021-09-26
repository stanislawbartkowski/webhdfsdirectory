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
| USERDIR | Root directory in HDFS. Directory to download is a subdirectory of USERDIR. Parameter active only for -u | /warehouse

# Two modes

The list of HDFS directories to be downloaded can be specifield two ways. The tool can scan the remote HDFS tree using WebHDFS REST API or the list of files and directories can be read from text file. In the second case, the WebHDFS REST API is used to download HDFS file, the HDFS tree is not scanned.

# Usage, list of of files is obtained using WebHDFS REST API

> ./hdfsdownload.sh -u hdfsdir localdir (optional)dryrun) (optional) regular expression to select directories for downloading

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

USERDIR=/user

> ./hdfsdownload.sh -u /user/sb /tmp/download


The downloaded directory structure
> tree /tmp/download/
```
/tmp/download/
└── sb
    ├── dir1
    │   ├── dir11
    │   │   └── hello11.txt
    │   └── hello.txt
    ├── dir11
    │   └── my11.txt
    └── dir2
        └── hello2.txt

```

Dryrun<br>
> ./hdfsdownload.sh -u /user/sb /tmp/download 1

# Usage, HDFS directory tree read from text file

This option should be used if scanning remote HDFS directory using WebHDFS REST/API fails because of time-out. Firstly the list of files and directories should be obtained by running *hdfs dfs -ls -R* command and output should be shipped to the node where tools is executed.<br>
<br>
> ./hdfsdownload.sh -l textfile localdir (optional)dryrun) (optional) regular expression to select directories for downloading

*textfile* should be the standard output of *hdfs dfs -ls* command.<br>

Parameters description<br>

| Parameter | Description | Sample value |
| -------- | ---------- | ----------- |
| textfile | Text file containing the list of HDFS tree | /tmp/hdfsoutput.txt
| localdir | as above
| dryrun (optional) | as above
| regexp (optional) | as above

# Several remarks

* In case of any error an exception is thrown and downloading is stopped.
* Application does not clean the local directory, if local directory is not empty then the content is overwritten.
* Empty HDFS directories are not recreated in local directory
