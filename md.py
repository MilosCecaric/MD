import json

class MD:
    def __init__(self):
        self.students = {}
        self.name = None
        self.filename = 'md.json'
        try:
            with open(self.filename, 'r') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = {}


    def add_student(self):
        name = input("Write name of new student: ")
        self.students[name] = []
        self.save_data()

    def go_(self, name):
        if name in self.students:
            self.name = name
            print(f"You have selected a student {name}.")
        else:
            print(f"student {name} does not exist.")

    def rename(self):
        students_name = input("Write new name of student: ")
        self.students[students_name] = self.students.pop(self.name)
        self.name = students_name
        self.save_data()

    def add_mark(self):
        mark = input("Write mark for student: ")
        valid_ratings = ['1', '1+', '1-', '2', '2+', '2-', '3', '3+', '3-', '4', '4+', '4-', '5', '5+', '5-']
        if mark in valid_ratings:
            self.students[self.name].append(mark)
        else:
            print("That rating is not supported.")
        self.save_data()

    def view_students(self):
        print("List of students: ")
        for name in self.students:
            print(name)

    def view_marks(self):
        if not self.students[self.name]:
            print(f"student {self.name} no rating registered.")
        else:
            print(f"Grades for a student {self.name}:")
            for mark in self.students[self.name]:
                print(mark)

    def exit_student(self):
        self.name = None
        print("Exited student.")

    def remove_student(self):
        if self.name in self.students:
            del self.students[self.name]
            self.name = name
            print(f"student {self.name} has been removed.")
        else:
            print(f"student {self.name} does not exist.")
        self.save_data()
    
    def remove_mark(self):
        if self.students[self.name]:
            print(f"Grades for a student {self.name}:")
            for index, mark in enumerate(self.students[self.name]):
                print(f"{index + 1} = {mark}")
            mark_for_delete = int(input("Enter the number of the grade to remove: "))
            if mark_for_delete in range(1, len(self.students[self.name]) + 1):
                del self.students[self.name][mark_for_delete - 1]
                print("Grade removed.")
            else:
                print("Invalid input, please try again.")
        else:
            print(f"student {self.name} no rating registered.")
        self.save_data()
            
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f)

md = MD()

while True:
    command = input("Write command: ")

    if command == "add_student":
        md.add_student()

    elif command.startswith("go_"):
        name = command.split("_")[1]
        md.go_(name)

    elif command == "rename":
        md.rename()

    elif command == "add_mark":
        md.add_mark()

    elif command == "view_students":
        md.view_students()

    elif command == "view_marks":
        md.view_marks()

    elif command == "remove_student":
        md.remove_student()
        
    elif command == "remove_mark":
        md.remove_mark()

    elif command == "exit_student":
        md.exit_student()

    elif command == "exit":
        break

    else:
        print("Unknown command, please check your command.")
