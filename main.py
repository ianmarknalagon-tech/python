class Student:

    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def display_info(self):
        """Prints the student's details in the specified format."""
        print("Student Information")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year}\n")

    def update_year_level(self, new_year):
        """Updates the year level and prints confirmation."""
        self.year = new_year
        print("Year level updated successfully!\n")


student1 = Student("Juan Dela Cruz", "BS Information Technology", 1)
student2 = Student("Maria Santos", "BS Computer Science", 2)
student3 = Student("Pedro Garcia", "BS Information Technology", 3)

print("STUDENT 1")
student1.display_info()

print("STUDENT 2")
student2.display_info()

print("STUDENT 3")
student3.display_info()

print("UPDATING STUDENT 1")
student1.update_year_level(3)

print("UPDATED STUDENT 1")
student1.display_info()