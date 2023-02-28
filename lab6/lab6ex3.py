from random import randint
# import random module

def main():
    # Creates a random list
    list_random = random_list()
    print("random list :", list_random)

    # gets max and min of the list
    print("max :", max(list_random), ", min :", min(list_random))

    # sums all elements of the list
    print("sum of the list :", sum(list_random))


def random_list():
    # initialize the list
    list_random = []

    # generates a random number between 0 and 100 for each element of the list
    for i in range(30):
        list_random.append(randint(0, 100))
    return list_random


if __name__ == '__main__':
    main()
