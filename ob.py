class Student:
    grade = 10
    name = "Alex"

    def introduction(self):
        print("Hello! I am a student.")

    def display_details(self):
        print("Student Name:", self.name)
        print("Student Grade:", self.grade)


student1 = Student()
student1.introduction()
student1.display_details()