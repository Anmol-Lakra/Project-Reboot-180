def display_title():
    print("=" * 35)
    print("          Notes Manager")
    print("=" * 35)
    print()

def display_menu():
    while True:
        print("1. Add Note")
        print("2. View  Notes")
        print("3. Exit\n")

        try:
            choice = int(input("Enter your  choice: ").strip())

        except ValueError:
            print("Invalid input - Choose correctly from  the menu.\n")

        else:
            if choice < 1 or choice > 3:
                print("Invalid Input - Choose correctly from the menu.\n")
            else:
                print()
                return choice
            

def get_note():
    while True:
        note = input("Enter note: ").strip()
        if note == "":
            print("Invalid input - Note cannot be blank.\n")
        else:
            return note


def save_note(note):
    try:
        file = open("notes.txt", "a")
        file.write(note + "\n")

    except PermissionError:
        return False

    else:
        file.close()
        return True


def view_notes():
    try:
        file = open("notes.txt", "r")
        data = file.read()

    except FileNotFoundError:
        print("Error. The file was not found.\n")

    else:
        print("\n----The contents of notes.txt----")
        print(data)
        file.close()

        
def main():
    display_title()

    while True:
        menu_choice = display_menu()
        if menu_choice == 1:
            note = get_note()

            is_saved = save_note(note)
            if is_saved:
                print("Note saved successfully.\n")
            else:
                print("Note did not save successfully.\n")

        elif menu_choice == 2:
            view_notes()

        else:
            break

    print("\nThank you for using Notes Manager.\n")        

main()