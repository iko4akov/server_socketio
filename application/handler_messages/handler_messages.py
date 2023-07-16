from random import randint
class Handler:

    def __init__(self):
        self.word = None
        self.next_user = None



    def get_index_user(self, users: list) -> int:
        index_user = randint(0, len(users))
        print(index_user)
        return index_user



    def check_sid(self, sid, data):
        pass

    def check_word(self, sid: str, data: dict, users: list):
        if self.word and self.next_user:
            if self.next_user['sid'] == sid:
                if self.word[-1].lower == data.get('word').lower:
                    return


        else:
            random_index = randint(0, len(users))
            self.word = data.get('word')
            self.next_user = users[random_index]
            return self.word, self.next_user
