source ./resource.rc
source ./commonproc.sh
touchlogfile

printhelp() {
    echo "hdownload.sh Download HDFS directory tree using WebHDFS Rest/API (non-secure)"
    echo 
    echo "Usage:"
    echo "hdownload.sh hdfsdir localdir (optional)dryrun (optional)dir_regular_expression"
    echo "hdfsdir : HDFS subdir of WEBHDFSUSERDIR to download"
    echo "localdir : local directory "
    exit
}

main() {
    required_listofvars "WEBHDFSHOST WEBHDFSPORT WEBHDFSUSER USERDIR DIRSCRIPT"
    HDFSDIR=$1
    LOCALDIR=$2
    DRYRUN=$3
    REGEXP=$4
    [ -z $HDFSDIR ] && printhelp
    [ -z $LOCALDIR ] && printhelp
    [ -z $DRYRUN ] && DRYRUN=0
    python3 $DIRSCRIPT/download.py $WEBHDFSHOST $WEBHDFSPORT $WEBHDFSUSER $USERDIR $HDFSDIR $LOCALDIR $DRYRUN $REGEXP
}

test() {
  # DRYRUN  
  main tablespace /tmp/xxxxx 1
  # DOWNLOAD
  # main tablespace /tmp/xxxxx 
}

main $@
#test

