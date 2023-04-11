class Student:
    # initializer
    def __init__(self, first_name="Sean", last_name="Griffin"):
        # initializer of Student class
        # arguments first_name and last_name are used to initialize class variables
        self.first_name = first_name
        self.last_name = last_name


# initialize a student with first name and last name at default value
student1 = Student()

# initialize a student with parameters for first name and last name
student2 = Student("Théo", "Fourré")

# initialize a student with parameters for first name and default value for last name
student3 = Student("Guillaume")
print(student1.first_name, student1.last_name)
print(student2.first_name, student2.last_name)
print(student3.first_name, student3.last_name)
