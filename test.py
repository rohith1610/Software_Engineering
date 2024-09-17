#hello team this is test file!!!!!
# Database class to store users - @SasidharKadiyala
class Database:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.user_id in self.users:
            print(f"User ID {user.user_id} already exists.")
        else:
            self.users[user.user_id] = user
            print(f"User {user.name} added successfully.")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User ID {user_id} deleted.")
        else:
            print(f"User ID {user_id} does not exist.")

    def update_user(self, user_id, name, email):
        if user_id in self.users:
            self.users[user_id].name = name
            self.users[user_id].email = email
            print(f"User ID {user_id} updated.")
        else:
            print(f"User ID {user_id} does not exist.")

    def get_users(self):
        return list(self.users.values())