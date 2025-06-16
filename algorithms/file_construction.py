import json

def file2b(path):
    return open(path, 'rb').read()


def b2file(data, file_name):
    a = open(f'/Users/mac/PycharmProjects/dec_cl_stor/test_files/{file_name}.ARW', 'wb')



def create_config(file_name, data):
    file = open(f'../config_files/{file_name}.json', 'w', encoding='utf-8')
    json.dump(data, file, indent=4)

def get_config(file_name):
    file = open("data.json", "r", encoding="utf-8")
    return json.load(file)