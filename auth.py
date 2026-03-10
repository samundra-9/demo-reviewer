def login(password):
    # FIX: Don't hardcode passwords!
    secret_key = "12345-ABCDE-SECRET" 
    if password == secret_key:
        print("Access Granted")
    else:
        print("Access Denied")