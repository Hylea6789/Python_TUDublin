#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################

def input_student_data(student_dic):
    student_id_in_dic = False

    # while the user inputs a student ID that is already in the dictionary
    while not student_id_in_dic:
        student_id = input("Enter the student ID : ")

        # if student id entered is not in the dictionary
        if student_id not in student_dic:
            student_id_in_dic = True
        else:
            print("Error : a student with this ID is in the dictionary")

    # input name, course and mark
    student_name = input("enter the student name : ")
    student_course = input("enter the student course : ")
    student_mark = int(input("enter the student mark : "))

    # adds a tuple with all student information to the student with the good ID
    student_dic[student_id] = (student_name, student_course, student_mark)


if __name__ == '__main__':
    # initialize student dictionary
    student_dic = {}

    # for the 5 students
    for i in range(5):
        print("input data for student", i + 1)
        input_student_data(student_dic)

    print(student_dic)
