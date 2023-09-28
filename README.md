# MD

# Program Documentation: MD

## Table of Contents

1. [Introduction](#introduction)
2. [Program Description](#program-description)
3. [Usage](#usage)
4. [Command List](#command-list)
5. [File Storage](#file-storage)
6. [Error Handling](#error-handling)
7. [Exiting the Program](#exiting-the-program)
8. [Conclusion](#conclusion)

---

## 1. Introduction<a name="introduction"></a>

The **MD** is a Python program designed to help users manage and organize student information and their corresponding grades. It allows users to create and manage student records, record grades, rename students, view student lists, view grades, remove students, remove grades, and save all data to a JSON file for future use.

## 2. Program Description<a name="program-description"></a>

The program uses a class named `MD` to encapsulate its functionality. Here is an overview of the main features:

- **Initialization**: When the program starts, it initializes an empty dictionary `students` to store student information and sets the `name` attribute to `None`. It attempts to load any existing data from a JSON file named 'md.json'.

- **Add Student**: Users can add a new student to the system by providing the student's name. A new student entry is created in the `students` dictionary.

- **Select Student**: Users can select a student by name using the `go_` command followed by the student's name. This sets the `name` attribute to the selected student's name for subsequent operations.

- **Rename Student**: Users can rename the currently selected student.

- **Add Mark**: Users can add grades (marks) to the currently selected student. The program validates the input and only accepts valid ratings.

- **View Students**: Users can view a list of all registered students.

- **View Marks**: Users can view the grades (marks) of the currently selected student.

- **Remove Student**: Users can remove the currently selected student from the system.

- **Remove Mark**: Users can remove a specific grade (mark) from the currently selected student's record.

- **Save Data**: The program saves all student data to a JSON file named 'md.json' whenever any changes are made.

## 3. Usage<a name="usage"></a>

To use the program, follow these steps:

1. Run the Python script containing the program.

2. Enter commands as specified in the [Command List](#command-list) section below.

3. The program will provide feedback and execute the requested operations.

4. To exit the program, use the `exit` command.

## 4. Command List<a name="command-list"></a>

- `add_student`: Adds a new student to the system.
- `go_<student_name>`: Selects a student by name.
- `rename`: Renames the currently selected student.
- `add_mark`: Adds a grade (mark) to the currently selected student.
- `view_students`: Displays a list of all registered students.
- `view_marks`: Displays the grades (marks) of the currently selected student.
- `remove_student`: Removes the currently selected student from the system.
- `remove_mark`: Removes a specific grade (mark) from the currently selected student's record.
- `exit_student`: Exits the currently selected student's context.
- `exit`: Exits the program.

## 5. File Storage<a name="file-storage"></a>

The program stores all student data in a JSON file named 'md.json' in the same directory as the script. This file is automatically created and updated as students and their grades are added or modified.

## 6. Error Handling<a name="error-handling"></a>

The program handles errors gracefully. It checks for invalid input, such as unrecognized commands and incorrect grade formats, and provides appropriate error messages to the user.

## 7. Exiting the Program<a name="exiting-the-program"></a>

To exit the program, simply enter the `exit` command. This ensures that all data is saved to the 'md.json' file before exiting.

## 8. Conclusion<a name="conclusion"></a>

The **MD** is a user-friendly Python program for managing student records and grades. It allows users to perform various operations on student data, ensuring data persistence through JSON file storage. The program provides clear feedback and handles errors to enhance the user experience.
