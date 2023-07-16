from random import randint

from application.models.users import Users


class HandlerMessages:

    def __init__(self):
        self.word = None
        self.answer_name = None
        self.answer_sid = None

    def check_sid(self, sid: str):
        """Проверка тот ли пользователь отвечает который должен """
        if sid == self.answer_sid:
            return True

    def set_params(self, sid: str, data: dict):
        """
        Устанавливает параметры:
        params:
        self.word -- слово с последней буквы которого необходимо назвать следующее слово
        self.answer_name -- имя пользователя кто должен отвечать следующий
        self.answer_sid -- sid пользовоателя который должен отвечать следующий
        """
        self.word = data.get('word')
        index = randint(0, len(Users.all_users)) - 1
        user = Users.all_users[index]
        self.answer_name = user['user_name']
        self.answer_sid = user['sid']

    def check_word(self, data: dict):
        """Проверка совпадения первой и последней букв по правилам игры"""
        if self.word[-1].lower() == str(data.get('word'))[0].lower():
            return True

    def check(self, sid: str, data: dict):
        """В случае корректности первых двух условий устанавливает новые параметры согласно функции set_params"""
        if self.check_sid(sid):
            if self.check_word(data):
                self.set_params(sid, data)
                return True
        else:
            return False
