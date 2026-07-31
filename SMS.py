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
        if self.marks>30:
            print("PASS")
        else:
            print("FAIL")

student1 = Student("Aayush",23,78)

student1.display_details()
student1.update_marks(30)
student1.pass_fail()