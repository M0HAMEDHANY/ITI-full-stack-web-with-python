from db.connection import get_db_connection

def delete_project(user_id):
    project_id = int(input("Enter project ID to delete: "))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM projects WHERE id = %s AND user_id = %s", (project_id, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()

    print("Project deleted successfully!")
