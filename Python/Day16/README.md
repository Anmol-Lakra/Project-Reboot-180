Project-Reboot-180 — Day 16
Nested Dictionaries and Student Management System
Day Overview
Day 16 focused on using nested dictionaries to organize related information and building a menu-driven Student Management System. The project combines dictionary operations, loops, conditionals, functions, input validation, searching, and basic statistics in one application.
Topics and Concepts Practised
- Nested dictionaries and accessing values inside inner dictionaries
- Iterating through dictionaries with .items()
- Adding, updating, and deleting dictionary information
- Searching student records by ID, information field, value, or course
- Using loops and conditional statements to control program flow
- Using Boolean flags to track whether records or matches were found
- Counting values dynamically with a dictionary counter
- Calculating total, average, youngest, and oldest age
- Validating numeric and text input
- Handling invalid numeric input with try / except ValueError
- Organizing a program into functions
- Building a menu-driven application
Project: Student Management System
The application stores student records in a nested dictionary. Each student has an ID and may have fields such as name, age, and course.
Menu Features
1. Display all students
2. Search for information about a specific student
3. Update a student's information
4. Delete a field from a student's record
5. Delete a student record
6. Find students by an information field and value
7. Display student statistics
8. Display course distribution
9. Find students enrolled in a course
10. Exit the application
Input Validation
- Rejects blank text input.
- Rejects text input consisting entirely of digits where text is expected.
- Validates numeric input and rejects values below 1.
- Converts age input to an integer after successful validation.
- Handles missing student IDs and missing information fields with messages.
Statistics and Search
The application can:
- Find matching students by a selected information field, such as name, age, or course.
- Count students enrolled in each course.
- Display the total number of students.
- Calculate average age, youngest age, and oldest age using the available age values.
- Handle records that are missing age or course information.
Important Implementation Note
Student records are stored in memory in the program's dictionary. Changes made while the application is running are not saved to a file or database, so the original sample records are loaded again when the program is restarted.
Skills Demonstrated
By completing this project, I practised:
- Structuring data with nested dictionaries
- Writing functions with clear responsibilities
- Implementing CRUD-style operations
- Searching and filtering records using loops and conditions
- Validating input and handling invalid numeric values
- Aggregating data using counters and totals
- Considering empty data and missing-field cases
- Combining multiple Python concepts into a single application
Day 16 Outcome
Built and reviewed a working, menu-driven Student Management System using nested dictionaries. The project brings together data management, searching, validation, and statistics in a single Python program.
Project Status
Day 16: Completed — Student Management System
The next day will begin only when I explicitly start it with the command Project Reboot - Day 17.