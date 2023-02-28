#######################
# Name : Sean GRIFFIN
# Date : 21/02/23
#######################

# Input string
string_to_reverse = input("Enter a string: ")

# string initialization
string_reversed = ""

# counts all the way from the length of string to 0
for i in range(len(string_to_reverse), 0, -1):
    string_reversed += string_to_reverse[i-1]

print("the string written in reverse is :", string_reversed)