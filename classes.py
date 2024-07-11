class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"I can walk"
    def __str__(self):
        return f"{self.name}"
    
# person1 = Person("Jon", 25)
# print(person1)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = []

    def enrol(self, course):
        self.course.append(course)
        return f"{self.name} enrolled in {self.course}"

    def __str__(self):
        return f"{self.name} {self.age} {self.student_id} {self.walk()}"
       
# student1 = Student("Ben", 30, 2)
# print(student1.enrol("Maths"))
# print(student1.enrol("English"))

class Undergraduate(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major =major
    
    def enrol(self, course):
        if len(self.course) < 2:
            return super().enrol(course)
        else:
            return f"Cannot enrol {self.name} in {self.course}"
    def __str__(self):
        return f"{self.name} {self.age} {self.student_id} {self.major}"
        
ungrad = Undergraduate("sarah", 18, 2, "Tech")
# # print(ungrad)
# print(ungrad.enrol("SE"))
# # print(ungrad.enrol("Economics"))
# # print(ungrad.enrol("Art"))
# print(ungrad.enrol("IT"))

def new_enrolment(student, course):
    return student.enrol(course)

enroll = new_enrolment(ungrad, "Spanish")
enroll = new_enrolment(ungrad, "G")

print(enroll)
