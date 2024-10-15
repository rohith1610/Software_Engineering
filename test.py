# <<<<<<< sheetalphuyal_add-class
# =======
# # User class
# class User:
#     def __init__(self, user_id, name, email):
#         self.user_id = user_id
#         self.name = name
#         self.email = email

#     def __str__(self):
#         return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


# # Database class to store users
# class Database:
#     def __init__(self):
#         self.users = {}

#     def add_user(self, user):
#         if user.user_id in self.users:
#             print(f"User ID {user.user_id} already exists.")
#         else:
#             self.users[user.user_id] = user
#             print(f"User {user.name} added successfully.")

#     def delete_user(self, user_id):
#         if user_id in self.users:
#             del self.users[user_id]
#             print(f"User ID {user_id} deleted.")
#         else:
#             print(f"User ID {user_id} does not exist.")

#     def update_user(self, user_id, name, email):
#         if user_id in self.users:
#             self.users[user_id].name = name
#             self.users[user_id].email = email
#             print(f"User ID {user_id} updated.")
#         else:
#             print(f"User ID {user_id} does not exist.")

#     def get_users(self):
#         return list(self.users.values())


# # UserManager class to handle user-related operations
# class UserManager:
#     def __init__(self):
#         self.db = Database()

#     def add_user(self, user_id, name, email):
#         user = User(user_id, name, email)
#         self.db.add_user(user)

#     def delete_user(self, user_id):
#         self.db.delete_user(user_id)

#     def update_user(self, user_id, name, email):
#         self.db.update_user(user_id, name, email)

#     def list_users(self):
#         return self.db.get_users()


# # Utility functions
# def validate_email(email):
#     if "@" in email and "." in email.split('@')[-1]:
#         return True
#     return False

# def validate_user_id(user_id):
#     if isinstance(user_id, int) and user_id > 0:
#         return True
#     return False


# # Main application
# def main():
#     user_manager = UserManager()

#     while True:
#         print("\nUser Management System")
#         print("1. Add User")
#         print("2. Delete User")
#         print("3. Update User")
#         print("4. List Users")
#         print("5. Exit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             user_id = int(input("Enter User ID: "))
#             name = input("Enter Name: ")
#             email = input("Enter Email: ")

#             if validate_user_id(user_id) and validate_email(email):
#                 user_manager.add_user(user_id, name, email)
#             else:
#                 print("Invalid user ID or email.")
        
#         elif choice == '2':
#             user_id = int(input("Enter User ID to delete: "))
#             if validate_user_id(user_id):
#                 user_manager.delete_user(user_id)
#             else:
#                 print("Invalid user ID.")
        
#         elif choice == '3':
#             user_id = int(input("Enter User ID to update: "))
#             name = input("Enter new Name: ")
#             email = input("Enter new Email: ")

#             if validate_user_id(user_id) and validate_email(email):
#                 user_manager.update_user(user_id, name, email)
#             else:
#                 print("Invalid user ID or email.")

#         elif choice == '4':
#             users = user_manager.list_users()
#             if users:
#                 for user in users:
#                     print(user)
#             else:
#                 print("No users found.")

#         elif choice == '5':
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()
# >>>>>>> main
