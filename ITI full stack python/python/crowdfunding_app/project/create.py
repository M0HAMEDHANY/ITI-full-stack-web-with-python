from db.connection import get_db_connection
def create_project(user_id):
    title = input("Project Title: ")
    details = input("Project Details: ")
    total_target = int(input("Total Target (EGP): "))
    start_time = input("Start Time (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("End Time (YYYY-MM-DD HH:MM:SS): ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO projects (user_id, title, details, total_target, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s)",
        (user_id, title, details, total_target, start_time, end_time)
    )
    conn.commit()
    cur.close()
    conn.close()

    print("Project created successfully!")
