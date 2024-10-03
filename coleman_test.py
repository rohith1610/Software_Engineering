class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        """Add a new user."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = user_data
        return f"User {user_id} added."

    def get_user(self, user_id):
        """Retrieve user information."""
        return self.users.get(user_id, "User not found.")

    def update_user(self, user_id, user_data):
        """Update user information."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        self.users[user_id] = user_data
        return f"User {user_id} updated."

    def delete_user(self, user_id):
        """Delete a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        del self.users[user_id]
        return f"User {user_id} deleted."

    def list_users(self):
        """List all users."""
        return self.users
    
    def to_html(self):
        """Generate an HTML representation of the users."""
        html_content = "<html><head><title>User List</title></head><body>"
        html_content += "<h1>User List</h1>"
        
        if not self.users:
            html_content += "<p>No users found.</p>"
        else:
            html_content += "<ul>"
            for user_id, user_data in self.users.items():
                html_content += f"<li>ID: {user_id}, Name: {user_data['name']}, Email: {user_data['email']}</li>"
            html_content += "</ul>"
        
        html_content += "</body></html>"
        return html_content

# Example usage to write HTML
if __name__ == "__main__":
    user_manager = UserManager()
    
    # Add some users
    user_manager.add_user("1", {"name": "Alice", "email": "alice@example.com"})
    user_manager.add_user("2", {"name": "Bob", "email": "bob@example.com"})
    
    # Generate HTML content
    html_content = user_manager.to_html()
    
    # Write HTML content to a file
    with open("users.html", "w") as file:
        file.write(html_content)
    
    print("HTML file 'users.html' created.")
