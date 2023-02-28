#######################
# Name : Sean GRIFFIN
# Date : 14/02/23
#######################

def main():
    # Calls the function read_port and stores its output in tcp_port
    tcp_port = read_port()

    # prints the tcp_port entered
    print("TCP port entered :", tcp_port)


def read_port():
    # input of the tcp port and conversion of it in an int
    tcp_port = int(input("Enter a valid TCP port between 0 and 1023 : "))

    # while the TCP port is not between 0 and 1023, forces the user to input a new one
    while tcp_port < 0 or tcp_port > 1023:
        print("Error : TCP number invalid")
        tcp_psort = int(input("Please enter again a valid TCP port between 0 and 1023 : "))
    return tcp_port


# Calls main function
main()
