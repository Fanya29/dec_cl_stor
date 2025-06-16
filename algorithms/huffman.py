from algorithms.bin_tree import *
from algorithms.sort import sort
from algorithms.file_construction import *

def archive(file_code, file_name):
    tree_table = _frequency_table(file_code)
    create_config(tree_table, file_name)
    return _table_replaces(tree_table, file_code)

def unarchieve(file_code, file_name):
    data = ''
    table = get_config(file_name)
    data = _table_replaces(table, file_code)
    b2file(data, file_name)


def _frequency_table(code):
    a = {}
    for i in range(0, len(code), 2):
        a[code[i] + code[i + 1]] = a.get(code[i] + code[i + 1], 0) + 1
    sorted_a = dict(sorted(a.items(), key=lambda item: item[1]))
    return _binary_tree(sorted_a)

def _binary_tree(table):
    nodes_dict = []
    for char in table:
        nodes_dict.append(create(char, table[char]))
    root_node = _nodes_compare(nodes_dict)
    _set_numerical(root_node)
    return _get_table(nodes_dict)

def _nodes_compare(nodes):
    while len(nodes) != 1:
        nodes.append(compare(nodes[0], nodes[1]))
        nodes = nodes[2:]
        if len(nodes) > 1:
            sort(nodes)
    return nodes[0]

def _set_numerical(node):
    node.left.numeric += '0'
    if node.left.left != None:
        _set_numerical(node.left)
    node.right.numeric += '1'
    if node.right.right != None:
        _set_numerical(node.right)

def _get_table(nodes):
    table = {}
    for node in nodes:
        table[node.data] = node.numeric
    return table

def _table_replaces(table, data):
    new_data = ''
    j = 0
    for i in range(1, len(data)):
        if data[j:i] in table:
            new_data += table[data[j:i]]
            i, j = i-1
    return new_data


def _reverse_table(table):
    new_table = {}
    for el in table:
        new_table[table[el]] = el
    return new_table


