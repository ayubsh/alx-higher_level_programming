#!/usr/bin/python3

def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        if (ord(tmp[i]) >= 97 and ord(tmp[i]) <= 122):
            tmp[i] = chr(ord(tmp[i]) - 32)
    print("{}".format("".join(tmp)))
