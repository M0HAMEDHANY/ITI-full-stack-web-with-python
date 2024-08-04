from db.connection import get_db_connection
def view_projects():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT p.id, p.title, p.details, p.total_target, p.start_time, p.end_time, u.first_name, u.last_name FROM projects p JOIN users u ON p.user_id = u.id"
    )
    projects = cur.fetchall()

    for project in projects:
        print(
            f"ID: {project[0]}, Title: {project[1]}, Details: {project[2]}, Target: {project[3]} EGP, Start: {project[4]}, End: {project[5]}, Owner: {project[6]} {project[7]}"
        )

    cur.close()
    conn.close()
