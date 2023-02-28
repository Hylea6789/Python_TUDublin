# User is asked to input a number, it is converted to an int
number = int(input("please enter a number between 5 and 20 : "))

# The while loop starts only if the number is out of boundaries
# The while loop will only stop if the number the user entered is between 5 and 20
while number < 5 or number > 20:
    print("ERROR : number entered out of boundaries")
    number = int(input("please enter again a number between 5 and 20 : "))

# The loop starts at number, finishes at 1, and is decremented of 1 for each loops
# the loop doesn't finish at 0 to have a prettier displaying
for i in range(number, 0, -1):
    # prints "i, " in the console
    print(i, end=', ')

# this is to display "0" and not "0, " a the end
print(0)