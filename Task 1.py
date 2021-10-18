#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def te():
    number = int(input("Введите число: "))
    if number > 0:
        positive()
    else:
        negative()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


if __name__ == '__main__':
    te()
