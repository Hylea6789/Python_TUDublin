# Sean GRIFFIN
# 07/02/23

# input of the port value and conversion of it to an integer
port = int(input("enter a port number between 0 and 65535 : "))

if port > 65535:    # if port number too high
    print("The port number is too high")
elif port < 0:  # if port number too low
    print("The port number is too low")
else:   # Port number is not too high or too low => port number is correct
    print("Valid port number")
