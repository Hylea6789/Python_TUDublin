#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################


# process one line of the file
def process_line(line, price_list, price_below_list):

    # takes the mark
    price = int(line.split(' ')[1])

    # input the list of price
    price_list.append(price)
    if price < 60:
        # stores a tuple with the id and the price in a list
        price_below_list.append((line.split(' ')[0][:5], line.split(' ')[1]))

def process_file():
    # initialize list
    price_list = []
    price_below_list = []

    # open the file
    with open("devices.txt") as devices_file:
        # for each line in the file
        for line in devices_file:
            process_line(line, price_list, price_below_list)

    # compute the average thanks to the sum and length of the list
    average_price = sum(price_list)/len(price_list)

    return price_list, price_below_list, average_price

if __name__ == '__main__':
    price_list, price_below_list, average_price = process_file()

    # prints a list with every prices
    print("price list :")
    print(price_list)

    # prints prices below 60€
    print("price below 60 euros")
    print(price_below_list)

    # prints the average
    print("average :", average_price)