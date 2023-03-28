
class Student:
   def __init__(self):
       # Constructor of the class Student
       print("---New Student---")

       # initialize the attributes first_name and last_name of class Student
       self.first_name = input("Enter the student first name : ")
       self.last_name = input("Enter the student last name : ")

# initialize a empty list of student
student_list = []

for i in range(3):
    student_list.append(Student())
    print(student_list[i].first_name, student_list[i].last_name)