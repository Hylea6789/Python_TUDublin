#######################
# Name : Sean GRIFFIN
# Date : 21/02/23
#######################

# checks if string_to_check contains the word spam
def check_spam(string_to_check):
    if "spam" in string_to_check:
        return True
    else:
        return False

# Function that returns the 5 first characters of string_to_slice
def string_slicing(string_to_slice):

    # Checks if the length of the string is below 5
    if len(string_to_slice) <= 5:
        string_sliced = string_to_slice
    else:
        string_sliced = string_to_slice[0:5]
    return string_sliced


def main():
    # string input
    string_to_slice = input("input a string: ")

    # string slicing
    string_sliced = string_slicing(string_to_slice)

    # if spam is in the 5 first characters displays a message to the user
    if check_spam(string_sliced):
        print("The 5 first characters of string \"", string_to_slice, "\" contains spam", sep="")
    else:
        print("The 5 first characters of string \"", string_to_slice, "\" does not contains spam", sep="")


if __name__ == '__main__':
    main()