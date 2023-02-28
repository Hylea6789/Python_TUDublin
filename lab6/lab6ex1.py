#######################
# Name : Sean GRIFFIN
# Date : 28/02/23
#######################

def main():
    # initialization of list
    my_list = [10, 11, 12, 13, 11]
    display_list(my_list)


def display_list(list_to_display):
    # display function of the list
    print("the list contains : ", end="")

    # i will contain each elements of the list
    for i in list_to_display:
        print(i, end=" ")
    print("")


if __name__ == '__main__':
    main()
