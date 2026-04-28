def login(password):
    secret = "my_secret_key"
    if password == secret:
        print("Access Granted")
    else:
        print("Access Denied")
