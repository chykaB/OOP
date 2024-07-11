from classes import *
def new_enrolment(student, course):
    return student.enrol(course)

enroll = new_enrolment(ungrad, "Spanish")
enroll = new_enrolment(ungrad, "G")