

def input_student_data(student_dic):
    student_id_in_dic = False
    while not student_id_in_dic:
        student_id = input("Enter the student ID : ")
        if student_id not in student_dic:
            student_id_in_dic = True
        else:
            print("Error : a student with this ID is in the dictionary")
    student_name = input("enter the student name : ")
    student_course = input("enter the student course : ")
    student_mark = int(input("enter the student mark : "))

    student_dic[student_id] = (student_name,student_course,student_mark)

if __name__ == '__main__':
    student_dic = {}
    for i in range(5):
        print("input data for student", i+1)
        input_student_data(student_dic)

    print(student_dic)