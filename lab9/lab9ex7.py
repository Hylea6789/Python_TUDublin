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

# student file name
STUDENT_FILE_NAME = "studentMarks.txt"

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
                # return the name of the grade
                return grade[0]

    def __str__(self):
        # string method for printing the Student class
        return "{first name : " + self.__first_name + ", last name : " + self.__last_name + ", marks : " + str(
            self.__marks) + "}"


if __name__ == '__main__':
    student_list = []
    # opens the file in read mode
    student_file = open(STUDENT_FILE_NAME, 'r')
    # skips header line
    student_file.readline()

    # for each lines of the file
    for line in student_file:
        # splits the line at each commas, permits to have a list with each value to add
        line_split = line.split(",")

        # initialize the student
        student = Student(line_split[0], line_split[1])

        # for the 3 marks
        for i in range(2, 5):
            student.add_mark(int(line_split[i]))
        student_list.append(student)

    for student in student_list:
        print(student)

