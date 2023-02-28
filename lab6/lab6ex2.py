#######################
# Name : Sean GRIFFIN
# Date : 28/02/23
#######################

def main():
    # ask the user to input the number
    my_list = input_numbers()

    # id of the list in main function, this list will be passed to square_list as an argument
    print("id of list in function 'main' :", id(my_list))

    # squares the list
    square_list(my_list)
    print(my_list)


def input_numbers():
    # initialize the list
    list_returned = []
    print("id of list in function 'input number' :", id(list_returned))

    # asks the user to input 10 float numbers
    for i in range(10):

        # each float number is first converted from a string to a float
        # each number is appended to list
        list_returned.append(float(input("enter the number {0} : ".format(i + 1))))
    return list_returned

# returns a list with all elements of list squared
def square_list(list_to_square):
    list_squared = []
    print("id of list in function 'square list' :", id(list_to_square))
    # each element of the input list is squared
    for element in list_to_square:
        list_squared.append(element ** 2)

    return list_squared


if __name__ == '__main__':
    main()
