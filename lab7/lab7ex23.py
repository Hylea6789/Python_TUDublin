#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

def main():
    write_file()
    write_file_john()


def write_file():
    # open the file in writing mode => Any file with this name will be erased
    file_to_write = open("name.txt", "w")

    # writes ten time a name in the file
    for i in range(10):
        # writes the input of the user
        file_to_write.write(input("enter a name : "))

        # writes an EOL
        file_to_write.write("\n")
    file_to_write.close()


def write_file_john():
    # open a file in appen mode => new data will be added at the end of the file
    file_to_write = open("name.txt", "a")

    # writes John Doe at the end of the file
    file_to_write.write("John Doe")
    file_to_write.close()


if __name__ == '__main__':
    main()
