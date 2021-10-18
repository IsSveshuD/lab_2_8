#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def cylinder(r, h):
    from math import pi
    def circle(r): return pi * r ** 2

    s = 2 * pi * r * h
    if input('Хотите получить полную площадь? Если откажетесь, \
    то будет выведена площадь боковой поверхности цилиндра. [y/n]: ') == 'y':
        s += 2 * circle(r)
    return s


if __name__ == '__main__':
    r = int(input("Введите радиус: "))
    h = int(input("Введите высоту: "))
    print('s =', cylinder(r, h))
