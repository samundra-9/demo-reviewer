# This is an example of a Python file violating the provided style guide.

def get_user(id):
    try:
        if id == 1:
            return "Alice"
        elif id == 2:
            return "Bob"
        else:
            raise Exception("User not found.")
    except Exception as e:
        print(e)
        return None

def main():
    user_id = int(input("Enter user ID: "))
    user_name = get_user(user_id)
    if user_name is not None:
        print(f"User Name: {user_name}")
    else:
        print("Failed to retrieve user info.")

main()