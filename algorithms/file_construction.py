import json

def file2b(name, extantion):
    return open(f'/Users/mac/PycharmProjects/dec_cl_stor/test_files/{name}.{extantion}', 'rb').read()


def b2file(data, file_name, extantion):
    a = open(f'/Users/mac/PycharmProjects/dec_cl_stor/test_files/{file_name}.{extantion}', 'wb')
    byte_data = bytes.fromhex(data)
    a.write(byte_data)

def create_config(data, file_name):
    file = open(f'/Users/mac/PycharmProjects/dec_cl_stor/config_files/{file_name}_data.json', 'w', encoding='utf-8')
    json.dump(data, file, indent=4)

def get_config(file_name):
    file = open(f'/Users/mac/PycharmProjects/dec_cl_stor/config_files/{file_name}_data.json', "r", encoding="utf-8")
    return json.load(file)