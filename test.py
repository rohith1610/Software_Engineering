# David Coleman's code
# UserManager class to handle user-related operations
class UserManager:
    def __init__(self):
        self.db = Database()

    def add_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.db.add_user(user)

    def delete_user(self, user_id):
        self.db.delete_user(user_id)

    def update_user(self, user_id, name, email):
        self.db.update_user(user_id, name, email)

    def list_users(self):
        return self.db.get_users()