def display_title():
    print("=" * 35)
    print("         Robust Notes Saver")
    print("=" * 35)
    print()

def get_note():
    while True:
        note = input("Enter note: ").strip()
        if note == "":
            print("Invalid input: Note cannot be blank.\n")
        else:
            return note

def save_note(data):
    try:
        file = open("notes.txt", "a")
        file.write(data + "\n")

    except PermissionError:
        return False

    else:
        file.close()
        return True

def main():
    display_title()
    user_note = get_note()
    is_saved = save_note(user_note)

    if is_saved:
        print("Note was saved successfully.\n")
    else:
        print("Note was not saved successfully.\n")

    print("Thank you for using Robust Notes Saver.\n")

main()