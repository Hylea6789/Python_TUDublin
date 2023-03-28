#######################
# Name : Sean GRIFFIN
# Date : 28/03/23
#######################

class Student:
    def __init__(self, first_name, last_name):
        # initializer of Student class
        # arguments first_name and last_name are used to initialize class variables
        self.__first_name = first_name
        self.__last_name = last_name

    def get_first_name(self):
        # getter for first name
        return self.__first_name

    def get_last_name(self):
        # getter for last name
        return self.__last_name

    def __str__(self):
        # string method for printing the Student class
        return "{First name : " + self.__first_name + ", last name : " + self.__last_name + "}"


student = Student("Sean", "Griffin")
print(student.get_first_name())
print(student.get_last_name())
print(student)
