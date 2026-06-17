def validate_username(username):
    if len(username) < 5:
        raise ValueError("Username must be at least 5 characters long")
    return True

def validate_email(email):
    if "@" not in  email or "." not in email:
        raise ValueError("Invalid email format. Must contain '@' and '.'")
    return True

def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be a least 8 characters long.")
    return True


username = input("Enter the username:..............")
email = input("Enter the email:................")
password = input("Enter the password:..........")


try:
    validate_username(username)
    validate_email(email)
    validate_password(password)

    print("Registration Successful!")

except ValueError as e:
    print(f"Registration failed: {e}")
