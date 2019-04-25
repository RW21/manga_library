import json
from pprint import pprint


def open_json(file) -> dict:
    with open(file) as jsonfile:
        data = json.load(jsonfile)

    return data


def write_json(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def get_last_index(file):
    data = open_json(file)

    # dictionaries are unordered
    return sorted(data.keys())[-1]


# print(get_last_index(r'C:\Users\RW\Desktop\code\manga_library\data.json')
# )