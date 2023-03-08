#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

# opens the file in reading mode. The file will be automatically closed at the end
with open("name.txt", "r") as file_to_read:
    # reads the first line
    line = file_to_read.readline()

    # while the line is not empty
    while line:
        # prints a line
        print(line, end="")

        # reads the next line of the file
        line = file_to_read.readline()