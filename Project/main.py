from ipwhois import IPWhois
# import IPWhois form ipwhois library

# file name with ddos log
FILE_DDOS = "DDoSRawLog.txt"

# file name with ip address
FILE_IP = "ip_adress.txt"

# file name for the report
FILE_REPORT = "Report.txt"


def generate_ip_file():

    # open ddos log file in read mode
    file_ddos = open(FILE_DDOS, "r")
    # open ip file in write mod, we will write here each ip address
    file_ip = open(FILE_IP, "w")

    # reads every lines in file_ddos and extract IP address
    for line in file_ddos:
        # splits the list on character "[" and take the third item
        # splits the list on character " " and take the third item
        # writes the IP address extracted on a new line in the file
        file_ip.write((line.split("]")[2].split(" ")[2] + "\n"))

    # close ddos log file
    file_ddos.close()

    # open ip file
    file_ip.close()


def class_ip(ip_address):
    # returns the class of an IP address

    # extract the first octet of the IP address
    first_octet = int(ip_address.split(".")[0])

    # Checks if class A
    if first_octet <= 127:
        ip_class = "A"

    # Checks if class B
    elif first_octet <= 191:
        ip_class = "B"

    # Checks if class C
    elif first_octet <= 223:
        ip_class = "C"

    # Checks if class D
    elif first_octet <= 239:
        ip_class = "D"

    # Checks if class E
    else:
        ip_class = "E"

    return ip_class


def generate_report():
    # open ip file in read mod
    file_ip = open(FILE_IP, "r")
    # open report file in write mode
    file_report = open(FILE_REPORT, "w")

    for line in file_ip:
        line = line.strip("\n")
        ip = IPWhois(line)
        ip_whois = ip.lookup_rdap()
        ip_class = class_ip(line)
        line_to_write = "{0} {1}| country = {2}, description = {3}\n".format(line, ip_class,
                                                                             ip_whois["asn_country_code"],
                                                                             ip_whois["asn_description"])
        file_report.write(line_to_write)

    file_ip.close()
    file_report.close()


generate_ip_file()
generate_report()
