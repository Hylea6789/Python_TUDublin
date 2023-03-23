FILE_JSON = "ifacedata.json"


def process_value(value):
    print(value)


    if value == "true":
        value_processed = True
    elif value == "false":
        value_processed = False
    elif value.find('"') != -1:
        value_processed = value.split('"')[1]
    else:
        value_processed = int(value)

    return value_processed


def read_json():
    file_json = open(FILE_JSON, "r")
    json = file_json.read()

    dic_json = {}
    list_json = json[1:-3].split(",")

    for item in list_json:
        key = item.split('"')[1]
        value = process_value(item.split(": ")[1])
        dic_json[key] = value

    file_json.close()
    return dic_json

if __name__ == '__main__':
    dic_json = read_json()
    print("Dictionnary")
    print(dic_json)