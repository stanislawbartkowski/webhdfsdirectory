# webhdfsdirectory

The application downloads HTTP directory recursively with subdirectories. It uses WebHDFS or HttpFS Rest/API interface. Current implementation is using only non-secure connection.

# Installation 

> git clone https://github.com/stanislawbartkowski/webhdfsdirectory.git

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
| USERDIR | Root directory in HDFS for file downloading | /warehouse

# Usage 


