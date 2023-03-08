#######################
# Name : Sean GRIFFIN
# Date : 07/03/23
#######################

x = int(input("enter an integer : "))
try:
    # asks the user for input and convert it to an integer
    x = int(input("enter an integer : "))
except:
    # If the number isn't an integer, displays an error message
    print("ERROR : you did not enterd an integer")
else:
    # If the number is an integer, displays the number
    print("you have entered :", x)