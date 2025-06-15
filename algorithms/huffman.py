from bin_tree import *
from sort import sort

def archive(file_code):
    tree_table = _frequency_table(file_code.hex())

def unarchieve():
    pass

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
    return _get_table(root_node)

def _nodes_compare(nodes):
    while len(nodes) != 1:
        del nodes.append(compare(nodes[0], nodes[1]))[0:2]
    return nodes[0]

def _get_table(node):
