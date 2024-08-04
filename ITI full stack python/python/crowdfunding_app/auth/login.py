from db.connection import get_db_connection

def login_user():
    email = input("Email: ")
    password = input("Password: ")

    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return None

    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, password, is_active FROM users WHERE email = %s", (email,)
        )
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result is None:
            print("No user found with this email.")
            return None

        user_id, stored_password, is_active = result

        if not is_active:
            print("Account is inactive.")
            return None

        if password == stored_password:
            print("Login successful!")
            return user_id
        else:
            print("Invalid credentials.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
