# 📘 Project Reboot - Day 13

## Exception Handling

---

## 📅 Day Overview

Day 13 introduced **Exception Handling**, an important concept for building reliable and robust Python applications.

Until now, most programs assumed that the user would provide valid input and that files or operations would work correctly.

On Day 13, we learned how to **anticipate errors, handle them safely, and prevent programs from crashing unexpectedly**.

This marks an important transition from programs that simply work under normal conditions to programs that can also deal with unexpected situations.

---

# 📚 Topics Covered

## Why Exception Handling?

Programs can encounter errors while running.

For example:

* A user enters text instead of a number.
* A program tries to divide by zero.
* A file does not exist.
* A file cannot be accessed because of permissions.
* An operation receives an invalid value.

Without exception handling, these situations can terminate the program.

Exception handling allows us to detect these problems and respond appropriately.

---

# ⚠️ Types of Errors

## Syntax Errors

Syntax errors occur when Python cannot understand the structure of the code.

Example:

```python
if age >= 18
    print("Adult")
```

The missing `:` causes a syntax error.

---

## Logical Errors

Logical errors occur when the program runs successfully but produces an incorrect result because the logic is wrong.

Example:

```python
num1 = 10
num2 = 5

result = num1 - num2

print("Addition =", result)
```

The program runs, but the logic is incorrect because subtraction was used instead of addition.

---

## Runtime Errors

Runtime errors occur while the program is executing.

Example:

```python
num1 = 10
num2 = 0

print(num1 / num2)
```

This produces a `ZeroDivisionError`.

Exception handling is primarily used to handle these kinds of runtime problems.

---

# 🛡️ try and except

The basic structure of exception handling is:

```python
try:
    # Code that may cause an error
except:
    # Code that handles the error
```

Example:

```python
try:
    age = int(input("Enter your age: "))
    print("Age =", age)

except ValueError:
    print("Please enter a valid number.")
```

If the user enters something that cannot be converted into an integer, the program handles the error instead of crashing.

---

# 🎯 ValueError

`ValueError` occurs when a function receives a value of the correct type but an inappropriate value.

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")
```

Example invalid input:

```text
Enter a number: abc
Invalid input.
```

---

# ➗ ZeroDivisionError

`ZeroDivisionError` occurs when a number is divided by zero.

Example:

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 🔀 Multiple Exceptions

Different errors can be handled separately.

Example:

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

This allows the program to give a more appropriate response depending on what went wrong.

---

# 🧩 try / except / else

The `else` block runs when no exception occurs.

Structure:

```python
try:
    # Code that may cause an error

except:
    # Runs if an error occurs

else:
    # Runs if no error occurs
```

Example:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)
```

---

# 🔚 try / except / finally

The `finally` block runs whether an exception occurs or not.

Structure:

```python
try:
    # Code

except:
    # Error handling

finally:
    # Always runs
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")
```

---

# 📂 File Exception Handling

Exception handling can also be used with file operations.

Example:

```python
try:
    file = open("notes.txt", "r")
    data = file.read()
    print(data)
    file.close()

except FileNotFoundError:
    print("File not found.")
```

This prevents the program from crashing when the requested file does not exist.

---

# 🔐 PermissionError

`PermissionError` occurs when Python does not have permission to perform an operation on a file or directory.

Example:

```python
try:
    file = open("students.txt", "a")
    file.write("John - 20\n")
    file.close()

except PermissionError:
    print("Permission denied.")
```

---

# 🧠 Important Concepts Learned

* Errors can occur during program execution.
* Exception handling prevents programs from crashing unexpectedly.
* `try` contains code that may cause an exception.
* `except` handles an exception.
* Different exception types can be handled separately.
* `ValueError` can occur when invalid input is converted to a number.
* `ZeroDivisionError` occurs when dividing by zero.
* `FileNotFoundError` occurs when a requested file cannot be found.
* `PermissionError` occurs when an operation is not permitted.
* `else` runs when no exception occurs.
* `finally` runs regardless of whether an exception occurs.
* Exception handling makes programs more reliable and user-friendly.

---

# 💻 Practice Programs

## Practice Program 1

### ValueError Handling

Handled invalid numeric input using:

* `try`
* `except`
* `ValueError`

---

## Practice Program 2

### ZeroDivisionError Handling

Handled division by zero using:

* `try`
* `except`
* `ZeroDivisionError`

---

## Practice Program 3

### Multiple Exception Handling

Handled different types of errors using multiple `except` blocks.

---

## Practice Program 4

### try / except / else

Practiced using `else` when no exception occurs.

---

## Practice Program 5

### try / except / finally

Practiced using `finally` to execute code regardless of whether an error occurred.

---

## Practice Program 6

### Safe Calculator

Built a calculator that safely handles invalid input and division by zero.

Concepts:

* `input()`
* type conversion
* `try`
* `except`
* `ValueError`
* `ZeroDivisionError`

---

## Practice Program 7

### Safe File Reader

Built a program that safely reads a file and handles situations where the file cannot be found.

Concepts:

* File handling
* `try`
* `except`
* `FileNotFoundError`

---

## Practice Program 8

### Safe File Writer

Built a program that safely writes information to a file while handling permission-related errors.

Concepts:

* File handling
* Append mode
* `try`
* `except`
* `PermissionError`

---

## Practice Program 9

### Notes Manager

Improved the Notes Manager by combining:

* User input
* Functions
* Loops
* File handling
* Exception handling
* Input validation

---

## Practice Program 10

### Student Record

Built a program that:

* Accepts student name
* Accepts student age
* Saves the record to `students.txt`
* Uses append mode
* Handles invalid age input
* Handles permission errors
* Uses `else`
* Uses `finally`

Example:

```text
Enter student name: John
Enter student age: 20

Student record saved successfully.
```

---

# 🚀 Mini Project

## Robust Student Record Manager

The final practice combined concepts learned throughout the previous days with exception handling.

### Features

* Accept student information
* Validate numeric input
* Save student records permanently
* Append records without deleting existing data
* Handle invalid input
* Handle file-related errors
* Provide appropriate messages to the user
* Use `try`
* Use `except`
* Use `else`
* Use `finally`

---

# 🎯 Skills Gained

By the end of Day 13, I can:

* Identify common types of errors.
* Understand the difference between syntax, logical, and runtime errors.
* Use `try` and `except`.
* Handle `ValueError`.
* Handle `ZeroDivisionError`.
* Handle `FileNotFoundError`.
* Handle `PermissionError`.
* Handle multiple exceptions.
* Use `else` with exception handling.
* Use `finally`.
* Build safer user-input programs.
* Build safer file-handling programs.
* Combine exception handling with:

  * Variables
  * Strings
  * User Input
  * Conditional Statements
  * Loops
  * Functions
  * File Handling

---

# 🏆 Key Learning Outcomes

Day 13 marked another important step in the development of practical Python applications.

The programs built during this day demonstrated that real-world programs must not only perform the expected operations, but also handle situations where something goes wrong.

The final exercises combined concepts learned across multiple days:

* Variables
* Strings
* User Input
* Conditional Statements
* Loops
* Functions
* File Handling
* Exception Handling

This demonstrated how individual Python concepts can work together to create applications that are more reliable, predictable, and user-friendly.

---

# 📈 Progress

```text
Project Reboot

█████████████□□□□□□□□□□□□□□□□□  13 / 30 Core Days Completed
```

---

# ⏭️ Next Module

## Day 14

The next stage of **Project Reboot** will continue building on the Python foundation developed during Days 1–13.

---

> "Good programs handle the unexpected."
>
> — Project Reboot, Day 13
