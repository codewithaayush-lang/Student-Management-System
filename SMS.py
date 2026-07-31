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

    def display_all_students(self):
        for student in self.students:
            student.display_details()

    def search_student(self,roll):
        for student in self.students:
            if roll == student.roll:
                student.display_details()
                return
        print("No student found with that name!")

    def remove_student(self,roll):
        for student in self.students:
            if roll == student.roll:
                self.students.remove(student)
                print("Student removed successfully")
                return
        print("No student found with that roll number!")


#testing

management1 = StudentManagement()

s1 = Student("Aayush",146,90)
s2 = Student("Rahul",147,85)

management1.add_student(s1)
management1.add_student(s2)

management1.display_all_students()

management1.remove_student(146)

management1.display_all_students()