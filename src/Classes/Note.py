import datetime as dt


class Note:
    '''
    Класс "заметка", описывающий базовое поведение и атрибуты заметок
    '''

    def __init__(self, note_id: str, head="empty head", body="empty body",
                 date_created=dt.datetime.now(), date_edited=dt.datetime.now()):
        self.__id = note_id
        self.__head = head
        self.__body = body
        self.__date_created = date_created
        self.__date_edited = date_edited

    def set_head(self, new_head):
        self.__head = new_head

    def set_body(self, new_body):
        self.__body = new_body

    def get_id(self):
        return self.__id

    def get_head(self):
        return self.__head

    def get_created_date(self):
        return self.__date_created

    def edit(self, new_head, new_body):
        '''
        Метод, редактирующий заголовок и тело заметки
        :param new_head: новый заголовок
        :param new_body: новое тело заметки
        :return: не возвращает значение
        '''
        self.set_head(new_head)
        self.set_body(new_body)
        self.__date_edited = dt.datetime.now()

    def __str__(self):
        return "Идентификатор: \t{}\n" \
               "Заголовок: \t{}\n" \
               "Текст: \t{}\n" \
               "Дата создания: \t{}\n" \
               "Дата изменения: \t{}\n".format(
            self.__id, self.__head, self.__body,
            self.__date_created, self.__date_edited
        )

    @staticmethod
    def decode_note(data):
        if "Head" in data:
            return Note(data['ID'],
                        data['Head'],
                        data['Body'],
                        dt.datetime.fromisoformat(data['Created date']),
                        dt.datetime.fromisoformat(data['Edited date']))

    @staticmethod
    def encode_note(note):
        type_name = note.__class__.__name__
        if type_name == 'Note':
            return {'ID': note.__id,
                    'Head': note.__head,
                    'Body': note.__body,
                    'Created date': note.__date_created.isoformat(),
                    'Edited date': note.__date_edited.isoformat()}
        else:
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
