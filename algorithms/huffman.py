from algorithms.bin_tree import *
from algorithms.file_construction import *
from algorithms.encoder import *

def archive(path):
    metadatas = ((path.split('/'))[-1]).split('.')
    data = file2b(metadatas[0], metadatas[1]).hex()
    tree_table = _frequency_table(data)
    create_config(tree_table, metadatas[0])
    archieved_data = bin2hex(_table_replaces(tree_table, data))
    print(f'Сжатие прошло успешно: {len(archieved_data)} / {len(data)} - {round(len(archieved_data)/len(data), 1)}%')
    b2file(archieved_data , metadatas[0], '_' + metadatas[1])

def unarchieve(path):
    metadatas = ((path.split('/'))[-1]).split('._')
    archived_data = hex2bin(file2b(metadatas[0],'_' + metadatas[1]).hex())
    table = _reverse_table(get_config(metadatas[0]))
    data = _table_replaces(table, archived_data)
    b2file(data, metadatas[0], metadatas[1])
    print("Файл разархивирован")

def _frequency_table(code):
    a = {}
    for i in range(0, len(code), 2):
        a[code[i] + code[i + 1]] = a.get(code[i] + code[i + 1], 0) + 1
    sorted_a = dict(sorted(a.items(), key=lambda item: item[1]))
    return binary_tree(sorted_a)

def _table_replaces(table, data):
    new_data = ''
    j = 0
    for i in range(1, len(data) + 1):
        if data[j:i] in table:
            new_data += table[data[j:i]]
            j = i
    return new_data

def _reverse_table(table):
    new_table = {}
    for el in table:
        new_table[table[el]] = el
    return new_table
