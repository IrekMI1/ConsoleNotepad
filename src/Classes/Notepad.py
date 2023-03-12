import json
import src.Classes.Note as nt


class Notepad:
    '''
    Класс "блокнот", который описывает базовую функциональность
    '''

    def __init__(self):
        self.notes_list = []
        self.objects_list = []

    def export_to_js(self):
        '''
        Метод, который экспортирует все заметки блокнота в JS-файл
        :param note: заметка, содержащая данные
        :return: нет возвращаемого значения
        '''
        for obj in self.notes_list:
            self.objects_list.append(nt.Note.encode_note(obj))
        with open('testJS.json', 'w', encoding='utf-8') as file:
            json.dump(self.objects_list, file)

    def import_from_js(self):
        '''
        Метод, который импортирует заметки из файла JSON
        :return: нет возвращаемого значения
        '''
        with open('testJS.json', 'r', encoding='utf-8') as js_data:
            self.notes_list = json.load(js_data, object_hook=nt.Note.decode_note)

    def add_note(self, note):
        '''
        Метод, добавляющий заметку в блокнот
        :param note: заметка с информацией
        :return: нет возвращаемого значения
        '''
        self.notes_list.append(note)

    def find_by_id(self, note_id: str):
        '''
        Метод, который находит заметку по номеру
        :param note_id: номер заметки
        :return: зкметка искомым с номером mote_id
        '''
        for note in self.notes_list:
            if note.get_id() == note_id:
                return note
        return "Заметка не найдена."

    def find_by(self, parameter, value):
        if parameter == 'i':
            return self.find_by_id(value)
        if parameter == 'h':
            return self.find_by_head(value)


    def find_by_head(self, note_head):
        '''
        Метод, который находит заметку по заголовку
        :param note_head: заголовок заметки
        :return: заметка  с искомым заголовком note_head
        '''
        for note in self.notes_list:
            if note.get_head() == note_head:
                return note
        return "Заметка не найдена."

    def delete_note(self, note):
        '''
        Метод, удаляющий заметку из блокнота
        :param note:
        :return: нетвозвращаемого значения
        '''
        self.notes_list.remove(note)

    def show_notes(self):
        '''
        Выводит на консоль информацию о всех заметках
        :return: нет возвращаемого значения
        '''
        is_empty = True
        for note in self.notes_list:
            print(note)
            is_empty = False
        if is_empty:
            print("В блокноте нет записей.")

    def show_by_date(self, date_provided):
        '''
        Выводит заметки на консоль, созданные в определенную дату
        :param date_provided: дата создания заметки формата ГГГГ-ММ-ДД
        :return: нет возвращаемого значения
        '''
        status = False
        for note in self.notes_list:
            date = note.get_created_date().date().isoformat()
            if date == date_provided:
                status = True
                print(note)
        if status is not True:
            print("Заметки с датой создания {} не найдены.".format(date_provided))
