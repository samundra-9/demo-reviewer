# Violates Rule: Missing Type Hints
# Violates Rule: SQL Injection (String Concat)
# Violates Rule: Hardcoded Secret
def connect_to_db(user_input):
    db_password = "super-secret-password-123"
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    print(f"Connecting with {db_password} to run {query}")
    return query