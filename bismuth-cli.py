#!/usr/bin/python
import os, sys, getopt


def create_project(projectname):
    clone = "git clone git@github.com:vushu/bismuth_cpp.git"
    os.mkdir(projectname)
    os.chdir(projectname)
    os.system(clone)


def main (argv):

    print("use -h for help")
    print("use -n <projectname> to create new bismuth project")
    projectname = ''
    try:
        opts, args = getopt.getopt(argv, "hn:", ["nproject="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("To a make a new project do: bismuth-cli.py -n <projectname>")
            sys.exit()
        elif opt in ("-n", "--nproject"):
            projectname = arg
            print("created project: ", projectname)
            create_project(projectname)
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
