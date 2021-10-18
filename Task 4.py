#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def get_input():
    return input('Введите число: ')


def tes_input(n):
    try:
        n = int(n)
        return True
    except:
        return False


def str_to_int(n):
    return int(n)


def print_int(n):
    print(n)


if __name__ == '__main__':
    n = get_input()
    print(tes_input(n))
    print(str_to_int(n))
    print(print_int(n))
