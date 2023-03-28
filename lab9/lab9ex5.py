#######################
# Name : Sean GRIFFIN
# Date : 28/03/23
#######################

# initialization of a dictionary with Grade name a a key and
# min and maximum as a value
GRADE_GUIDE = {
    "Distinction": (70, 100),
    "Upper Merit": (60, 69),
    "Lower Merit": (50, 59),
    "Pass": (40, 49),
    "Fail": (0, 39)
}


class Student:

    def __init__(self, first_name, last_name):
        # initializer of Student class
        # arguments first_name and last_name are used to initialize class variables
        # marks is initialize an empty list
        self.__first_name = first_name
        self.__last_name = last_name
        self.__marks = []

    def get_first_name(self):
        # getter for first name
        return self.__first_name

    def get_last_name(self):
        # getter for last name
        return self.__last_name

    def set_first_name(self, first_name):
        # setter for first name
        self.__first_name = first_name

    def set_last_name(self, last_name):
        # setter for last name
        self.__last_name = last_name

    def add_mark(self, mark):
        # adds the argument mark to the mark list
        self.__marks.append((mark, self.convert_mark_grade(mark)))

    def convert_mark_grade(self, mark):
        for grade in GRADE_GUIDE.items():
            # extract the minimum and the maximum mark of a distinction
            min = grade[1][0]
            max = grade[1][1]
            if min <= mark <= max:
                return grade[0]

    def __str__(self):
        # string method for printing the Student class
        return "{first name : " + self.__first_name + ", last name : " + self.__last_name + ", marks : " + str(
            self.__marks) + "}"


student = Student("Sean", "Griffin")
print(student)
# adds 45 and 77 to the mark list
student.add_mark(45)
student.add_mark(77)

# Changes first and last name of student
student.set_first_name("Guillaume")
student.set_last_name("Louis")
print(student)
