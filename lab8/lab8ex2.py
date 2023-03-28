#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################

def main():
    # convert the file in a list
    list_ip = convert_file_list()
    print("list ip :", list_ip)

    # convert the list in a set
    set_ip = set(list_ip)
    print("set ip :", set_ip)

def convert_file_list():
    # initialize list
    list_ip = []

    # open ipaddress.txt in read mod
    with open("ipaddresses.txt", "r") as ip_file:
        # reads all the file and convert it in a list. \n is the separator used by the list
        list_ip = ip_file.read().splitlines()

    return list_ip


if __name__ == '__main__':
    main()
