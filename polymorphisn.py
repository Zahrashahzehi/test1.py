class I_user_servis:
    def get_All_users(self):
        raise NotImplementedError
    def get_user_by_id(self):
        raise NotImplementedError
    def creat_new_user(self):
        raise NotImplementedError
class user_servise_by_sql(I_user_servis):
    def get_All_users(self):
        print("get all user from sql . ")
class user_servise_by_oracle(I_user_servis):
    def get_All_users(self):
        print("get all user from oracle . ")
user_servise = user_servise_by_sql()
user_servise.get_All_users()
#user_servise.get_user_by_id()                                