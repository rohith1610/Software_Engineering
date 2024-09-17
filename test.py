# Utility functions
def validate_email(email):
    if "@" in email and "." in email.split('@')[-1]:
        return True
    return False

def validate_user_id(user_id):
    if isinstance(user_id, int) and user_id > 0:
        return True
    return False
