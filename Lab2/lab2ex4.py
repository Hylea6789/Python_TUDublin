# Sean GRIFFIN 31/01/23
mark = int(input("enter your mark : "))
if (mark < 0) | (mark > 100):
    print("Error : the mark must be between 0 and 100")
else:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    elif mark >= 50:
        grade = "E"
    else:
        grade = "F"

    print("your grade is ", grade)
