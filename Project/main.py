# import the class IPWhois from ipwhois library
from ipwhois import IPWhois

# file name with ddos log
FILE_DDOS = "DDoSRawLog.txt"
# file name with ip address
FILE_IP = "ip_address.txt"
# file name for the report
FILE_REPORT = "report.csv"


def main():
    # main function

    # generate the file containing all of the IP addresses
    generate_ip_file()
    # generate the report file
    generate_report()


def generate_ip_file():
    # generate a text file containing all of the IP addresses

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

    # closes ddos log file
    file_ddos.close()
    # closes ip file
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

    # returns the class of the IP address
    return ip_class


def whois_ip(ip_address):
    # return the country and description of an IP address thanks to whois command

    # create an IPWhois object with ip address parameter
    ip = IPWhois(ip_address)

    # uses the method lookup_rdap() of an IPWhois object
    # returns a dictionary containing the whois command result
    ip_whois = ip.lookup_rdap()

    # ip_whois result is stored in a dictionary, we just need to retrieve the country code and description from it
    return ip_whois["asn_country_code"], ip_whois["asn_description"]


def generate_report():
    # open ip file in read mod
    file_ip = open(FILE_IP, "r")
    # open report file in write mode
    file_report = open(FILE_REPORT, "w")

    # writes the header line of the report file
    file_report.write("address,class,country,description\n")

    # for each line of the file
    for line in file_ip:
        # deletes the final \n character
        ip_address = line.strip("\n")
        # gets the class of the IP address
        ip_class = class_ip(ip_address)
        # gets the country and description of the IP address
        ip_country, ip_description = whois_ip(ip_address)

        # format the line to write in the report containing the data of the IP address
        line_to_write = '{0},{1},{2},"{3}"\n'.format(ip_address, ip_class, ip_country,
                                                     ip_description)
        # writes the line in the report file
        file_report.write(line_to_write)

    # closes ip file
    file_ip.close()
    # closes report file
    file_report.close()


if __name__ == '__main__':
    main()
