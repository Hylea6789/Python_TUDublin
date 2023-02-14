# Sean GRIFFIN
# 07/02/23

# IP_ADD_STATIC contains the start of the IP address string
IP_ADD_STATIC = "192.168.1."

# For loop with i between 1 and 64
for i in range(1,64):
    # concatenate the start of the IP address with it's end (converted from string to int)
    ip_add = IP_ADD_STATIC + str(i)

    print(ip_add)