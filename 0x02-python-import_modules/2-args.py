#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arglen = len(sys.argv)
    if arglen == 1:
        print("0 arguments.")
    else:
        if arglen == 2:
            print("{:d} argument:".format(arglen - 1))
        else:
            print("{:d} arguments:".format(arglen - 1))
        for a in range(1, arglen):
            print("{}: {}".format(a, sys.argv[a]))
