import src.Classes.Notepad as NP
import src.Classes.Note as NT
import view


def start_notepad():
    '''
    Функция, которая отвечает за логику приложения "блокнот"
    :return: нет возвращаемого значения
    '''
    notepad = NP.Notepad()
    notepad.import_from_js()
    working_mode = view.get_mode()

    while working_mode != 'q':
        if working_mode == 'a':
            data = view.input_data()
            notepad.add_note(NT.Note(data[0], data[1], data[2]))
            print('Заметка добавлена.\n')

        elif working_mode == 'e':
            find_mode = view.find_mode()
            current_note = notepad.find_by(find_mode, view.get_value(find_mode))
            if isinstance(current_note, NT.Note):
                current_note.edit(view.get_new_head(), view.get_new_body())
                print("Заметка изменена.\n")
            else:
                print("Заметка не найдена.\n")

        elif working_mode == 's':
            notepad.show_notes()

        elif working_mode == 'd':
            find_mode = view.find_mode()
            current_note = notepad.find_by(find_mode, view.get_value(find_mode))
            if isinstance(current_note, NT.Note):
                notepad.delete_note(current_note)
                print("Заметка удалена.\n")
            else:
                print("Заметка не найдена.\n")

        elif working_mode == 'r':
            find_mode = view.find_mode()
            current_note = notepad.find_by(find_mode, view.get_value(find_mode))
            if isinstance(current_note, NT.Note):
                print(current_note)
            else:
                print("Заметка не найдена.\n")

        elif working_mode == 'f':
            date = input("Введите дату в формате ГГГГ-ММ-ДД: \t")
            notepad.show_by_date(date)

        working_mode = view.get_mode()
    notepad.export_to_js()
