from apis.user import user_instance


class RpcMethods:
    @staticmethod
    def get_users(*args, **kwargs):
        """
        Get user list
        :param args:
        :param kwargs:
        :return:
        """
        return user_instance.get_list()

    @staticmethod
    def get_user(*args, **kwargs):
        """
        Get user by id
        :param args:
        :param kwargs: id
        :return:
        """
        return user_instance.get(kwargs['id'])
