#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

# opens the document marks.txt in reading mode
with open("students.txt", "r") as student_file:
    # initialize the maximum at 0
    maximum = 0

    # reads each line of the file
    for line in student_file:

        # convert the string to an int
        try:
            mark = int(line.split(",")[2])

        except:
            # If it is the header line
            # It its the case it will not be able to convert "Mark" to a number
            mark = 0

        # if the mark read is superior to all previous marks, it is the new maximum
        if mark > maximum:
            maximum = mark
            max_student = line.replace(",", " ")

# displays the new maximum
print("the maximum is", max_student)