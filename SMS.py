class Student:
    def __init__(self,name,roll,marks):
        #initialize attributes
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No. {self.roll}")
        print(f"Marks: {self.marks}")
        self.pass_fail()

    def update_marks(self,newmarks):
        self.marks = newmarks

    def pass_fail(self):
        if self.marks>=30:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed")

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        print("Student added successfully")

    def display_all_students(self):
        if not self.students:
            print("No students available")
            return
        
        for student in self.students:
            student.display_details()

    def search_student(self,roll):
        for student in self.students:
            if roll == student.roll:
                student.display_details()
                return
        print("No student found with that roll no.!")

    def remove_student(self,roll):
        for student in self.students:
            if roll == student.roll:
                self.students.remove(student)
                print("Student removed successfully")
                return
        print("No student found with that roll number!")


#remove the testing portion if you dont want to test the Student Management List

# testing portion starts from here

# management1 = StudentManagement()

# s1 = Student("Aayush",146,90)
# s2 = Student("Rahul",147,85)

# management1.add_student(s1)
# management1.add_student(s2)

# management1.display_all_students()

# management1.remove_student(146)

# management1.display_all_students()

#testing portion ends here

# Menu driven interface

management = StudentManagement()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name of the student:")
        roll = int(input("Rollno. of the student:"))
        marks = int(input("Marks:"))
        student = Student(name,roll,marks)
        management.add_student(student)
    elif choice == "2":
        management.display_all_students()
    elif choice == "3":
        roll = int(input("Enter the roll no. of the student: "))
        management.search_student(roll)
    elif choice == "4":
        roll = int(input("Enter the roll nol of the student you want to remove: "))
        management.remove_student(roll)
    elif choice == "5":
        break
    else:
        print("Invalid menu choice! Please try again")
        