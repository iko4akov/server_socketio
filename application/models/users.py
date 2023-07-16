
class Users:

    all_users = []
    all_sids = []

    def __init__(self, data: dict, sid: str):
        self.sid = sid
        self.data = data
        self.check_user = self.__check_user()


    def __check_user(self):
        if self.sid not in self.all_sids:
            self.all_sids.append(self.sid)
            self.id = len(self.all_users) + 1
            self.user_name = self.data.get('player_name') + '_' + str(self.id)
            self.all_users.append(self.__dict__)
            return True

        else:
            return False
