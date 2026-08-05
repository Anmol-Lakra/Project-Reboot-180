def menu():
    print("=" * 40)
    print("             Notes Manager")
    print("=" * 40)

    print("1. Add Notes\n")
    print("2. View Notes\n")
    print("3. Exit\n")

    

def menu_selection():
    while True:
        user_input = input("Enter your choice: ").strip()
        if not user_input.isdigit():
            print("Invalid Input - Please choose from the option.\n")
        elif int(user_input) < 1 or int(user_input) > 3:
            print("Invalid Input - Please choose from the option.\n") 
        else:
            return int(user_input)

def add_notes():
    note = input("Enter note: ").strip()

    file = open("notes.txt", "a")

    file.write("\n" + note)

    file.close()

    print()

    print("Note added successfully.\n")

def view_notes():
    print("\nThe contents of the file are as follows:")

    file = open("notes.txt", "r")

    notes_in_file = file.read()

    print(notes_in_file)

    file.close()

    print()

        
def main():
    while True:
        menu()
        selected_menu = menu_selection()
        if selected_menu == 1:
            add_notes()
        elif selected_menu == 2:
            view_notes()
        else:
            break

    print("\nThank you for using Notes Manager.\n")    

main()