from db.connection import get_db_connection


def register_user():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    mobile_phone = input("Mobile Phone: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (first_name, last_name, email, password, mobile_phone, is_active) VALUES (%s, %s, %s, %s, %s, %s)",
            (first_name, last_name, email, password, mobile_phone, True),
        )
        conn.commit()
        cur.close()
        conn.close()
        print("User registered successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
        if cur:
            cur.close()
        if conn:
            conn.close()
