#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from datetime import date


def get_worker():
    """
    Запросить данные о работнике.
    """
    name = input("Фамилия и инициалы? ")
    post = input("Должность? ")
    year = int(input("Год поступления? "))
# Создать словарь.
    return {
        'name': name,
        'post': post,
        'year': year,
    }


 def display_workers(staff):
    """
    Отобразить список работников.
    """
# Проверить, что список работников не пуст.
    if staff:

        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Ф.И.О.",
                "Должность",
                "Год"
            )
        )
        print(line)
# Вывести данные о всех сотрудниках.
        workers = []
        for idx, worker in enumerate(workers, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    worker.get('name', ''),
                    worker.get('post', ''),
                    worker.get('year', 0)
                )
            )
        print(line)
    else:
        print("Список работников пуст.")


def select_workers(staff, period):
    """
    Выбрать работников с заданным стажем.
    """

    today = date.today()

    result = []
    for employee in staff:
        if today.year - employee.get('year', today.year) >= period:
            result.append(employee)
# Возвратить список выбранных работников.
    return result


def main():
    """
    Главная функция программы.
    """
# Список работников.
    workers = []
# Организовать бесконечный цикл запроса команд.
    while True:

        command = input(">>> ").lower()
# Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':

            worker = get_worker()

            workers.append(worker)
# Отсортировать список в случае необходимости.
        if len(workers) > 1:
            workers.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':

            display_workers(workers)
        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)

            period = int(parts[1])

            selected = select_workers(workers, period)
# Отобразить выбранных работников.
            display_workers(selected)
        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
    if __name__ == '__main__':
        main()
