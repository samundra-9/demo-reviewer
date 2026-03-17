def login(password):

    secret_key = "12345-ABCD" 
    if password == secret_key:
        print("Access Granted")
    else:
        print("Access Denied")