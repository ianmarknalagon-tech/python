class Course:
    def __init__(self, title, capacity):
        self.title = title
        self.capacity = capacity
        self.enrolled = 0

class Student:
    def __init__(self, name):
        self.name = name

    def enroll(self, course):
        course.enrolled += 1
        print(self.name, "enrolled in", course.title)

course1 = Course("Python 101", 30)
student1 = Student("Ana")
student1.enroll(course1)