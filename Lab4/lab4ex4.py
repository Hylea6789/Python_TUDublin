#######################
# Name : Sean GRIFFIN
# Date : 14/02/23
#######################

def main():
    # Calls the function read_port and stores its output in tcp_port
    tcp_port = get_port()

    # prints the tcp_port entered
    display_port(tcp_port)


def display_port(tcp_port):
    # prints the tcp_port
    print("TCP port entered :", tcp_port)

def is_valid_port(tcp_port):
    # checks if TCP port is between 0 and 1023
    if tcp_port < 0 or tcp_port > 1023:
        return False
    else:
        return True

def get_port():
    # input of the tcp port and conversion of it in an int
    tcp_port = int(input("Enter a valid TCP port between 0 and 1023 : "))

    # while the TCP port is not valid, forces the user to input a new one
    while not is_valid_port(tcp_port):
        print("Error : TCP number invalid")
        tcp_port = int(input("Please enter again a valid TCP port between 0 and 1023 : "))
    return tcp_port


# Calls main function
main()
