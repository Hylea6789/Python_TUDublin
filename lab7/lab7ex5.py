#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

# opens the document marks.txt in reading mode
with open("marks.txt", "r") as mark_file:
    # initialize the maximum at 0
    maximum = 0

    # reads each line of the file
    for line in mark_file:

        # convert the string to an int
        mark = int(line)

        # if the mark read is superior to all previous marks, it is the new maximum
        if mark > maximum:
            maximum = mark

# displays the new maximum
print("the maximum is", maximum)