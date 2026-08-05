# 📘 Project Reboot - Day 12
## File Handling

---

## 📅 Day Overview

Day 12 introduced one of the most important concepts in programming—**File Handling**.

Until now, every program stored data only while it was running. After the program ended, all variables were lost because they were stored in RAM.

On Day 12, we learned how to permanently store and retrieve information using text files.

This marks the transition from temporary programs to applications that can save and reuse data.

---

# 📚 Topics Covered

## Why File Handling?

- Variables are stored in RAM.
- RAM is volatile memory.
- Data stored in variables is lost when the program ends.
- Files allow programs to permanently store information on disk.

---

## File Handling Workflow

Every basic file program follows the same workflow:

```
Open File
     ↓
Read / Write
     ↓
Close File
```

---

## Opening a File

```python
file = open("notes.txt", "r")
```

Learned:

- `open()`
- File connection
- File object (basic understanding)

---

## Reading a File

```python
data = file.read()
```

Learned:

- `read()` returns the entire contents of the file.
- The returned value is stored in a variable.
- Displaying file contents using `print()`.

---

## Writing to a File

```python
file = open("notes.txt", "w")
```

Learned:

- `"w"` means Write Mode.
- Existing file contents are erased before writing.
- `write()` writes exactly what is provided.

---

## Appending to a File

```python
file = open("notes.txt", "a")
```

Learned:

- `"a"` means Append Mode.
- Existing data is preserved.
- New data is added to the end of the file.

---

## Closing a File

```python
file.close()
```

Learned:

- Release the file connection.
- Save pending operations.
- Good programming practice.

---

# 📂 File Modes Learned

| Mode | Purpose |
|------|---------|
| `"r"` | Read existing file |
| `"w"` | Write (replace existing contents) |
| `"a"` | Append (add new data) |

---

# 🧠 Important Concepts Learned

- Variables are temporary.
- Files are permanent.
- `open()` establishes a connection to a file.
- `read()` returns data.
- `write()` writes exactly the supplied string.
- `write()` does **not** automatically insert a new line.
- `"\n"` creates a new line.
- Always close a file after use.

---

# 💻 Practice Programs

### Practice Program 1

**Save User Name**

Concepts:

- input()
- append mode
- write()
- close()

---

### Practice Program 2

**Student Record Saver**

Concepts:

- Multiple input()
- String concatenation
- File writing
- Permanent storage

---

### Practice Program 3

**Read Student Records**

Concepts:

- Read Mode
- read()
- Display stored records

---

# 🚀 Mini Projects

## Mini Project 1

### Personal Notes Manager

Features:

- Accept user notes
- Store notes permanently
- Append without deleting previous notes

---

## Mini Project 2

### View Personal Notes

Features:

- Read all saved notes
- Display notes to the user

---

## Mini Project 3 (Capstone)

### Notes Manager

Features:

- Interactive menu
- Add notes
- View notes
- Exit application
- Input validation
- Function-based program design

---

# 🎯 Skills Gained

By the end of Day 12, I can:

- Create text files
- Read files
- Write files
- Append data
- Close files properly
- Build programs that permanently store user data
- Combine file handling with:
  - Variables
  - Strings
  - Functions
  - Loops
  - Input validation

---

# 🏆 Key Learning Outcomes

This day marked the transition from simple Python programs to applications capable of storing and retrieving permanent data.

The final Notes Manager project combined concepts learned across multiple days, including:

- Variables
- Strings
- User Input
- Conditional Statements
- Loops
- Functions
- File Handling

This demonstrated how individual programming concepts work together to build practical applications.

---

# 📈 Progress

```
Project Reboot

████████████□□□□□□□□  12 / 30 Core Days Completed
```

---

# ⏭️ Next Module

## Day 13

### Exception Handling

Upcoming topics:

- Runtime errors
- Syntax errors
- Logical errors
- try
- except
- finally
- Raising exceptions
- Building robust applications

---

> "Programs become truly useful when they can remember."
>
> — Project Reboot, Day 12