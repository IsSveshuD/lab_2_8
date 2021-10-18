#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def t():
    r = 1
    while 1:
        ch = int(input())
        if not ch: break
        r *= ch
        print(r)
    return (r)


if __name__ == '__main__':
    print(t())
