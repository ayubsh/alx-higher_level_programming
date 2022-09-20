#!/usr/bin/python3

def print_last_digit(number):
    ld = number % 10 if number > 0 else int(repr(number)[-1])
    print("{}".format(ld), end='')
    return ld
