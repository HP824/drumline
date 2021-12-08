from drumline.app.helpers import *


def print_help():
    print("""Available commands:
    * add (adds new member)
    * list (lists all existing members)
    * find (finds existing member)
    * remove (removes existing member)
    * promote (promotes drumline)
    * scramble (assigns random roles to all members)
""")


def main():
    print("Welcome to the Drumline utility!")
    print_help()
    print("A sample drumline has already been created for you.")
    while True:
        command = input(">>> ").lower()
        if command == "add":
            add_member()
        elif command == "list":
            list_members()
        elif command == "find":
            find_member()
        elif command == "remove":
            remove_member()
        elif command == "promote":
            promote_members()
        elif command == "scramble":
            scramble_members()
        elif command == "quit":
            break
        else:
            print("Invalid command.")
            print_help()
    print("Goodbye!")


if __name__ == "__main__":
    main()
