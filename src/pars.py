
def addargs(parser) :
    parser.add_argument('host', nargs=1, help='HDFS/FS host')
    parser.add_argument('port', nargs=1, help='HDFS/FS port', type=int)
    parser.add_argument('user', nargs=1, help='HDFS/FS user name')
    parser.add_argument('userdir', nargs=1, help='HDFS/FS root user dir')
    parser.add_argument('usersubdir', nargs=1, help='HDFS/FS user subdir dir')
    parser.add_argument('localdir', nargs=1,
                        help='Local directory to store files')
    parser.add_argument('--dryrun', nargs='?', type=bool, const="dryrun",
                        help='Treverse directory only, do not download',default=False)
    parser.add_argument('--regexp', nargs='?', type=str, const="regexp",
                        help='Regular expression')
