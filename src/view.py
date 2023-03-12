def input_data():
    message = [
        'Введите идентификатор заметки:\t',
        'Введите заголовок:\t',
        'Введите текст:\t',
    ]
    data = []
    for i in range(3):
        data.append(input(message[i]))
    return data


def get_mode():
    message = 'Выберите действие: \n' \
              '\ta - добавить заметку \n ' \
              '\td - удалить заметку \n ' \
              '\te - редактировать заметку \n ' \
              '\tf - фильтр по дате \n' \
              '\tr - показать заметку \n' \
              '\ts - показать все заметки \n ' \
              '\tq - выход\n'
    mode = input(message)
    while mode not in 'adefrsq':
        mode = input(message)

    return mode


def find_mode():
    message = "Выберите заметку: i - по номеру / h - по заголовку:\n"
    input_mode = input(message)
    while input_mode not in 'ih':
        input_mode = input(message)
    return input_mode


def get_value(mode):
    if mode == 'i':
        return get_id_input()
    if mode == 'h':
        return get_head_input()


def get_id_input():
    return input("Введите идентификатор: ")


def get_head_input():
    return input("Введите заголовок: ")


def get_new_head():
    return input("Введите новый заголовок: ")


def get_new_body():
    return input("Введите новый текст: ")
