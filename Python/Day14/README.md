# 📘 Project Reboot - Day 14

## Exception Handling, Robust Programs & Notes Manager

---

## 📅 Day Overview

Day 14 focused on taking the exception handling and file-handling concepts learned previously and combining them with **functions, loops, input validation, return values, and menu-driven program design**.

The objective was to move beyond individual Python exercises and begin building small, reliable applications.

Throughout the day, programs were designed using an **algorithm-first approach**:

```text
Understand
    ↓
Design Algorithm
    ↓
Implement
    ↓
Test
    ↓
Industry Code Review
    ↓
Improve
```

---

# 📚 Topics Covered

## 🟢 Exception Handling

* `try`
* `except`
* `else`
* `finally`
* `ValueError`
* `PermissionError`
* `FileNotFoundError`
* Handling invalid user input
* Handling file-related errors
* Preventing programs from crashing unexpectedly

---

## 🟢 Functions

* Defining functions using `def`
* Calling functions
* Function parameters
* Returning values
* Separating responsibilities between functions
* Function decomposition
* `main()` function
* Reusable functions

---

## 🟢 Loops

* `while True`
* Loop-based input validation
* `break`
* `continue`
* Using `return` to exit a function and loop
* Menu-driven loops

---

## 🟢 Input Validation

Practiced validating:

* Integer input
* Blank input
* Invalid menu choices
* File names
* User notes

Programs were designed to keep asking for valid input rather than terminating unexpectedly.

---

## 🟢 File Handling

Worked with:

* `open()`
* Read mode (`"r"`)
* Append mode (`"a"`)
* `read()`
* `write()`
* `close()`
* Permanent storage using text files
* File-related exception handling

---

## 🟢 Return Values

A major concept introduced during Day 14 was using return values to allow functions to communicate results to other functions.

Example:

```python
is_saved = save_note(note)

if is_saved:
    print("Note saved successfully.")
else:
    print("Note did not save successfully.")
```

The function performs the operation and returns a Boolean result:

```text
True  → Operation successful
False → Operation failed
```

This helped establish separation between **application logic and user-interface output**.

---

# 💻 Practice Programs

## 1. Safe Number Input

Created a program that:

* Asks the user for an integer
* Handles `ValueError`
* Continues asking until valid input is received
* Uses `while True`
* Uses `try / except`
* Uses `else`
* Uses `break`

---

## 2. Reusable Safe Number Input

Created a reusable:

```python
get_valid_number()
```

function.

The function:

* Accepts user input
* Handles `ValueError`
* Repeats until valid input is entered
* Returns the valid integer

The program also introduced:

```python
main()
```

to separate program control from input validation.

---

## 3. Safe File Reader

Created a program that:

* Accepts a filename
* Opens the file in read mode
* Reads file contents
* Displays the contents
* Handles `FileNotFoundError`
* Closes the file after successful reading

---

## 4. Safe File Writer

Created a program that:

* Accepts a filename
* Accepts user data
* Opens the file in append mode
* Writes data to the file
* Adds a newline after each entry
* Handles `PermissionError`
* Closes the file after successful writing

---

## 5. Robust Notes Saver

Created a program using multiple functions:

```text
display_title()
get_note()
save_note()
main()
```

Features:

* Rejects blank notes
* Accepts user notes
* Saves notes permanently
* Uses append mode
* Handles `PermissionError`
* Returns `True` or `False` from `save_note()`
* Uses `main()` to control the program

---

# 🚀 Mini Project

## Notes Manager

The final challenge of Day 14 was a complete **menu-driven Notes Manager**.

### Features

```text
1. Add Note
2. View Notes
3. Exit
```

### Add Note

The program:

* Accepts a note from the user
* Rejects blank notes
* Saves the note to `notes.txt`
* Uses append mode
* Handles `PermissionError`
* Reports whether the note was saved successfully

### View Notes

The program:

* Opens `notes.txt`
* Reads all saved notes
* Displays the contents
* Handles `FileNotFoundError`
* Closes the file after successful reading

### Exit

The program exits the menu loop when the user selects:

```text
3. Exit
```

---

# 🧩 Final Notes Manager Structure

```text
Notes Manager
│
├── display_title()
│
├── display_menu()
│     └── Validates menu choice 1–3
│
├── get_note()
│     └── Rejects blank notes
│
├── save_note()
│     └── Writes notes to notes.txt
│
├── view_notes()
│     └── Reads notes.txt
│
└── main()
      └── Controls the application
```

---

# 🧠 Important Concepts Learned

### Separation of Responsibilities

Each function should have a clear purpose.

```text
get_note()
    ↓
Get data

save_note()
    ↓
Save data

view_notes()
    ↓
Read data

display_menu()
    ↓
Get and validate menu choice

main()
    ↓
Control the application
```

---

### Function Communication

Functions can return information to their caller.

Example:

```python
note = get_note()
```

and:

```python
is_saved = save_note(note)
```

This allows different parts of the program to communicate without placing all logic inside one large function.

---

### Boolean Return Values

Used:

```python
True
False
```

to communicate whether an operation succeeded.

```text
save_note()
     ↓
 ┌───────┐
 │       │
True   False
 │       │
 ↓       ↓
Success Error
```

---

### Input Validation

Programs were designed to reject invalid input rather than crash.

Examples:

```text
Invalid integer
Blank note
Invalid menu choice
```

---

# 🏆 Skills Developed

By the end of Day 14, I can:

* Define and use functions.
* Pass arguments to functions.
* Return values from functions.
* Use Boolean return values.
* Build reusable functions.
* Use `while True`.
* Use `break`.
* Use `continue`.
* Use `try / except / else`.
* Handle `ValueError`.
* Handle `PermissionError`.
* Handle `FileNotFoundError`.
* Validate user input.
* Read text files.
* Write to text files.
* Append data to files.
* Close files properly.
* Build menu-driven applications.
* Separate program responsibilities into functions.
* Design algorithms before implementation.
* Test programs using edge cases.
* Improve code based on code review.

---

# 🧪 Edge Cases Practiced

Day 14 programs considered situations such as:

* User enters text instead of an integer.
* User enters an empty value.
* User enters a number outside the valid menu range.
* User attempts to open a file that doesn't exist.
* A file cannot be written because of permissions.
* A user attempts to save a blank note.
* A notes file contains previously saved data.

---

# 🏗️ Programming Practices Developed

Throughout Day 14, the following practices were emphasized:

* Algorithm-first development
* Small functions
* Clear function responsibilities
* Meaningful variable names
* Specific exception handling
* Input validation
* Separation of concerns
* Return values for communication
* Testing edge cases
* Code review
* Incremental improvement
* Avoiding unnecessary complexity

---

# 📊 Day 14 Progress

```text
Project Reboot

██████████████□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

14 / 180 Days Completed
```

### Current Milestone

**14 / 180 Days**

---

# 🏆 Day 14 Final Project

## Notes Manager

The final Notes Manager combines concepts learned across Project Reboot:

```text
Variables
   ↓
Strings
   ↓
Conditionals
   ↓
Loops
   ↓
Functions
   ↓
Lists
   ↓
Recursion
   ↓
File Handling
   ↓
Exception Handling
   ↓
Input Validation
   ↓
Return Values
   ↓
Menu-Driven Application
```

This represents the progression from learning individual Python concepts to combining them into a practical application.

---

# 📈 Project Progress

```text
Project Reboot-180

██████████████□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

Day 14 Completed
```

---

# ⏭️ Next Module

## 📘 Day 15

The next stage of Project Reboot will introduce **Dictionaries** and continue developing Python data-handling skills.

Upcoming concepts include:

* Dictionary creation
* Keys
* Values
* Accessing dictionary data
* Adding data
* Updating data
* Removing data
* Dictionary methods
* Iterating through dictionaries
* Nested dictionaries
* Practical applications

---

> **"A program becomes powerful when individual concepts work together."**
>
> — Project Reboot, Day 14
