#######################
# Name : Sean GRIFFIN
# Date : 21/02/23
#######################

# Function that ask the user to input a name and a mark between 0 and 100
# An error message is displayed until the mark inputed is between 0 and 100
def user_input():
    name = input("Name of the student : ")

    mark = int(input("Enter a mark between 0  and 100: "))
    while not check_mark_correct(mark):
        mark = int(input("Error : Enter again a mark between 0 and 100: "))
    return name,mark


# Function that returns True if the mark is between 0 and 100
def check_mark_correct(mark):
    if mark > 100 or mark < 0:
        return False
    else:
        return True

# Function that returns True if the mark is over 90
def check_medal(mark):
    # We already know that the mark is below 100, no need to check again
    if mark >= 90:
        return True
    else:
        return False

# Function that displays a message depending if the user has a medal or not
def display_medal(has_medal):
    if has_medal:
        print("Congratulations you have won a gold medal")
    else:
        print("sorry no medals today")


def main():
    # name and mark input
    name, mark = user_input()

    # Checks if user has a medal for his mark
    has_medal = check_medal(mark)

    # displays a message depending if the user has won a medal or not
    display_medal(has_medal)

if __name__ == '__main__':
    main()