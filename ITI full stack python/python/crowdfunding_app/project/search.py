from db.connection import get_db_connection

def search_projects_by_date():
    date = input("Enter date to search (YYYY-MM-DD): ")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, details, total_target, start_time, end_time FROM projects WHERE start_time::date <= %s::date AND end_time::date >= %s::date",
        (date, date),
    )
    projects = cur.fetchall()

    for project in projects:
        print(
            f"ID: {project[0]}, Title: {project[1]}, Details: {project[2]}, Target: {project[3]} EGP, Start: {project[4]}, End: {project[5]}"
        )

    cur.close()
    conn.close()
