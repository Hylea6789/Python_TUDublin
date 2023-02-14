# Sean GRIFFIN
# 07/02/23

# initialization of number
number = int(input("Please enter a number between 1 and 10 :"))

while number < 1 or number > 10: # while the number inputed is out of reach
    # If a loop starts ther is an error => an error message is displayed
    print("Error : number out of reach")
    number = int(input("Please enter a number between 1 and 10 :"))

# Final number
print("number =", number)