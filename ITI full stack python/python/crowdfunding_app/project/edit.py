from db.connection import get_db_connection

def edit_project(user_id):
    project_id = int(input("Enter project ID to edit: "))
    title = input("New Project Title: ")
    details = input("New Project Details: ")
    total_target = int(input("New Total Target (EGP): "))
    start_time = input("New Start Time (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("New End Time (YYYY-MM-DD HH:MM:SS): ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE projects SET title = %s, details = %s, total_target = %s, start_time = %s, end_time = %s WHERE id = %s AND user_id = %s",
        (title, details, total_target, start_time, end_time, project_id, user_id),
    )
    conn.commit()
    cur.close()
    conn.close()

    print("Project updated successfully!")
