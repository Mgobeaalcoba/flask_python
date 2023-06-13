from .firestore_service import get_user

from flask_login import UserMixin

class UserData():
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin): 
    def __init__(self, user_data: UserData):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod # Indica que es un metodo estatico. Es decir, no recibe self. 
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username = user_doc.id,
            password = user_doc.to_dict()['password']
        )

        return UserModel(user_data)
    
# class Todo():
#     def __init__(self, description) -> None:
#         self.description = description
