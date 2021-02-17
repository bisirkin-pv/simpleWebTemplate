import uuid


class UserInstance:
    def __init__(self):
        self._USERS = []

    def get_list(self):
        """
        Get all users as list
        :return: [UserModel]
        """
        return self._USERS

    def get(self, id: str):
        """
        Get user by Id
        :param id:
        :return: UserModel
        """
        for u in self._USERS:
            if u['id'] == id:
                return u
        return {}

    def create(self, data: dict):
        """
        Create new user
        :param data:
        :return: UserModel
        """
        uid = uuid.uuid4()
        new_user = {'id': str(uid)}
        for k, v in data.items():
            new_user[k] = v
        self._USERS.append(new_user)
        return new_user

    def update(self, id: str, data: dict):
        """
        Update user
        :param id:
        :param data:
        :return: UserModel
        """
        u = self.get(id)
        if u:
            for k, v in data.items():
                u[k] = v
            return u
        return {}

    def delete(self, id: str):
        """
        Delete user
        :param id:
        :return: Boolean
        """
        for i in range(len(self._USERS)):
            if self._USERS[i]['id'] == id:
                del self._USERS[i]
            return True
        return False
