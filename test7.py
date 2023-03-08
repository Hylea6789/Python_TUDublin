#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

# main program
def main():
    # input string
    string_number = input_number()

    # slice the input string in a list
    lst = split_string(string_number)

    # for each numbers of the list checks if it is greater than 100
    greater_100(lst)
    print("list :", lst)

    # sorts the list. The result is stored in lst
    lst.sort()
    print("sorted list :", lst)

    # thanks to the -1 step parameter, displays the list in reverse order
    print("list in reverse order :", lst[::-1])

    # slices the list
    print("sliced list : ", lst[:3])


# asks the user to input 5 numbers separated per commas
def input_number():
    string_number = input("enter a sequence of 5 numbers : ")
    return string_number


# splits the string in a list of number
def split_string(string_number):
    lst = string_number.split(",")
    lst_number = []
    for i in lst:
        lst_number.append(int(i))
    return lst_number

# checks for each elements in the list if it is greater than 100
def greater_100(lst):
    for num in lst:
        if num > 100:
            print("the value", num, "is greater then 100")


if __name__ == '__main__':
    main()
