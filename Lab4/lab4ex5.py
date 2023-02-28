def main():
    # input the parameters of rectangle
    # NOTE : the rectangle needs to have a width and length of at least 2, else the program doesn't work
    width = enter_parameter(2, "enter the width of the rectangle : ")
    length = enter_parameter(2, "enter the tength of the rectangle : ")

    # prints the top "width" line
    print_line_width(width)

    # prints the "length" line
    for i in range(length - 2):
        print_line_length(width)

    # prints the bottom "width" line
    print_line_width(width)


def enter_parameter(min, message_input):
    # permit the user to input a parameter, checks if it higher than the minimum
    is_not_correct = True
    while is_not_correct:
        parameter = int(input(message_input))
        if parameter < min:
            print("Error : enter again the value")
        else:
            is_not_correct = False
    return parameter


def print_line_length(width):
    # prints a line of width characters
    # prints a '#' on the first and width character
    # prints a ' ' on the second to width - 1 character
    print("")
    print("#", end="")
    for i in range(width - 2):
        print(" ", end="")
    print("#", end="")


def print_line_width(width):
    # prints a line of width characters
    # prints a full line of #
    print("")
    for i in range(width):
        print("#", end="")


main()
