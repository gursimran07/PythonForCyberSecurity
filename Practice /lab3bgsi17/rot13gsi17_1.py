#!/usr/bin/env python3


def print_ascii_table():
    for i in range(32, 127):
        print("{0} \t '{1}'".format(i, chr(i)))


print_ascii_table()
