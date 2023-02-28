##########################
# Name : Sean GRIFFIN
# Date : 14/02/23
##########################

def main():
    # Calls the get_three_value functiopn to initialize x, y, z
    x, y, z = get_three_values()

    # Calls the compute average function with the parameters set with x, y and z
    average = computeAverage(x, y, z) # average gets the return
    print("average of ", x, ", ", y, ", ", z, " is ", average, sep="")


def get_three_values():
    # asks the user to enter a value and convert it to a float
    x = float(input("enter the first value : "))
    y = float(input("enter the second value : "))
    z = float(input("enter the third value : "))
    return x, y, z


def computeAverage(x, y=0, z=0):
    # takes 3 values x, y, z and returns the average
    # The returned value is a float number
    # y and z have 0 in default value
    return (x + y + z)/3

# Calls the main function
main()