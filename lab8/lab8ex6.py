#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################

# name of the JSON file
FILE_JSON = "ifacedata.json"


def process_value(value):
    # process a value by determining if it is a boolean, string or integer
    print(value)

    # If boolean True
    if value == "true":
        value_processed = True

    # If boolean False
    elif value == "false":
        value_processed = False

    # If String
    elif value.find('"') != -1:
        value_processed = value.split('"')[1]

    # If integer
    else:
        value_processed = int(value)

    return value_processed


def read_json():
    # process a JSON file

    # open the file in read mode
    file_json = open(FILE_JSON, "r")
    json = file_json.read()

    # initialize the JSON dictionnary
    dic_json = {}

    # removes the first "{" and final "}\n"
    list_json = json[1:-3].split(",")

    for item in list_json:
        # extract the key
        key = item.split('"')[1]
        # extract and find data type of value
        value = process_value(item.split(": ")[1])
        # Puts a value in the JSON dictionary
        dic_json[key] = value

    file_json.close()
    return dic_json


if __name__ == '__main__':
    dic_json = read_json()

    # prints the dictionnary
    print("Dictionary")
    print(dic_json)
