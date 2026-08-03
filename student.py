from main import Student


class school:
    school = "Marvelous Collage"

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("juan", "BSIT")
student2 = Student("maria", "BSCS")

print (school.school)
print (student1.name)
print (student1.course)

print (school.school)
print (student2.name)
print (student2.course)