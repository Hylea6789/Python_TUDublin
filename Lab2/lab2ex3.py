# Sean GRIFFIN 31/01/23

# input the numbers
num1 = int(input("first number : "))
num2 = int(input("second number : "))
num3 = int(input("third number : "))

# determins the max
if (num1 >= num2) & (num1 >= num3): # num1 max ?
    num_max = num1
elif (num2 >= num1) & (num2 >= num3): # num2 max ?
    num_max = num2
else: # num1 and num2 aren't max => num3 max
    num_max = num3

# determins the min
if (num1 <= num2) & (num1 <= num3): # num1 min ?
    num_min = num1
elif (num2 <= num1) & (num2 <= num3): # num2 min ?
    num_min = num2
else:  # num1 and num2 aren't min => num3 min
    num_min = num3

print("max :", num_max)
print("min :", num_min)