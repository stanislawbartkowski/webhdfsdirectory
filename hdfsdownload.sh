source ./resource.rc
source ./commonproc.sh
touchlogfile

printhelp() {
    echo "hdownload.sh Download HDFS directory tree using WebHDFS Rest/API (non-secure)"
    echo 
    echo "Usage:"
    echo "hdownload.sh -u/-l  hdfsdir localdir (optional)dryrun (optional)dir_regular_expression"
    echo "-u Access WebHDFS for directory list"
    echo "-l Take directory list from text file"
    echo "hdfsdir : HDFS subdir of WEBHDFSUSERDIR to download"
    echo "localdir : local directory "
    echo ""
    echo "./hdfsdownload.sh -l dir11 /tmp/x --dryrun"
    echo "./hdfsdownload.sh -l dir11 /tmp/x"

    logfail "Incorrect parameter, cannot continue"
}

mainurl() {
    python3 $DIRSCRIPT/download.py $WEBHDFSHOST $WEBHDFSPORT $WEBHDFSUSER $USERDIR $HDFSDIR $LOCALDIR $DRYRUN $REGEXP
}

mainlist() {
    required_var INPUTTXT
    python3 $DIRSCRIPT/downloadlist.py $INPUTTXT $WEBHDFSHOST $WEBHDFSPORT $WEBHDFSUSER $USERDIR $HDFSDIR $LOCALDIR $DRYRUN $REGEXP
}

test() {
  # DRYRUN  
  main tablespace /tmp/xxxxx 1
  # DOWNLOAD
  # main tablespace /tmp/xxxxx 
}

main() {
  required_listofvars "WEBHDFSHOST WEBHDFSPORT WEBHDFSUSER USERDIR DIRSCRIPT"
  what=$1
  shift

  HDFSDIR=$1
  LOCALDIR=$2
  DRYRUN=$3
  REGEXP=$4
  [ -z $what ] && printhelp
  [ -z $HDFSDIR ] && printhelp
  [ -z $LOCALDIR ] && printhelp
#  [ -z $DRYRUN ] && DRYRUN=0
  
  case $what in
    -u) mainurl $@;;
    -l) mainlist $@;;
    *) printhelp;;
  esac
}

main $@
#test

