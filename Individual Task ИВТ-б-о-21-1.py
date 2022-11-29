#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def get_contact():
    """
    Запросить данные о человеке
    """
    family = input("Фамилия? ")
    name = input("Имя? ")
    number = int(input("Номер телефона? "))
    born = list(map(int, input("Дата рождения? ").split('.', 2)))

    return {
        'family': family,
        'name': name,
        'number': number,
        'born': born,
    }


def display_contact(contacts):
    """
    Отобразить спискок контактов
    """
    if contacts:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^30} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Номер телефона",
                "Дата Рождения"
            )
        )
        print(line)

        for idx, contact in enumerate(contacts, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<30} | {:>20} |'.format(
                    idx,
                    contact.get('family', ''),
                    contact.get('name', ''),
                    contact.get('number', 0),
                    '.'.join((str(i) for i in contact['born']))
                )
            )
        print(line)
    else:
        print("Список контктов пуст.")


def select_contact(contacts, period):
    """
    Выбрать маршрут
    """
    result = []
    for contact in contacts:
        if contact.get('family') == period:
            result.append(contact)

    return result


def main():
    """
    Главная функция программы
    """
    contacts = []

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            contact = get_contact()
            contacts.append(contact)
            if len(contacts) > 1:
                contacts.sort(key=lambda item: item.get('number', [0 - 2]))

        elif command == 'list':
            display_contact(contacts)

        elif command.startswith('select'):
            period = input('Введите Фамилию человека,'
                           ' информацию по которому Вы хотите найти: ')

            selected = select_contact(contacts, period)
            display_contact(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить контакт;")
            print("list - Вывести список контактов;")
            print("select -  Поиск по фамилии;")
            print("help - Отобразить справку;")
            print("exit - Завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
