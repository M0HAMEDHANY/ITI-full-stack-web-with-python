from auth.register import register_user
from auth.login import login_user
from project.create import create_project
from project.view import view_projects
from project.edit import edit_project
from project.delete import delete_project
from project.search import search_projects_by_date


def main():
    user_id = None
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Create Project")
        print("4. View Projects")
        print("5. Edit Project")
        print("6. Delete Project")
        print("7. Search Projects by Date")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = login_user()
            if user_id:
                print("Welcome")
        elif choice == "3":
            if user_id:
                create_project(user_id)
            else:
                print("You need to login first")
        elif choice == "4":
            view_projects()
        elif choice == "5":
            if user_id:
                edit_project(user_id)
            else:
                print("You need to login first")
        elif choice == "6":
            if user_id:
                delete_project(user_id)
            else:
                print("You need to login first")
        elif choice == "7":
            search_projects_by_date()
        elif choice == "8":
            break
        else:
            print("Invalid choice, Please try again")


if __name__ == "__main__":
    main()
