
def main():
    list_ip = convert_file_list()
    print(list_ip)


def convert_file_list():
    list_ip = []
    with open("ipaddresses.txt", "r") as ip_file:
        list_ip = ip_file.read().splitlines()

    return list_ip

def convert_list_set():
    print("HEY")

if __name__ == '__main__':
    main()
