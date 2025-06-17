from algorithms.sort import sort

class BinaryTree:
    pass

def create(data=None, value=None, right=None, left=None):
    a = BinaryTree()
    a.data = data
    a.value = value
    a.right = right
    a.left = left
    a.numeric = ''
    return a

def compare(node1, node2):
    if node1.value > node2.value:
        return create(None, node1.value+node2.value, node2, node1)
    else:
        return create(None, node1.value + node2.value, node1, node2)


def binary_tree(table):
    nodes_dict = []
    for char in table:
        if char != None:
            nodes_dict.append(create(char, table[char]))
    root_node = _nodes_compare(nodes_dict)
    _set_numerical(root_node)
    return _get_table(nodes_dict)

def _nodes_compare(nodes_dict):
    nodes = []
    for i in range(len(nodes_dict)):
        nodes.append(nodes_dict[i])
    while len(nodes) != 1:
        nodes.append(compare(nodes[0], nodes[1]))
        nodes = nodes[2:]
        if len(nodes) > 1:
            sort(nodes)
    return nodes[0]

def _set_numerical(node):
    node.left.numeric = node.numeric + '0'
    if node.left.left != None:
        _set_numerical(node.left)
    node.right.numeric = node.numeric + '1'
    if node.right.right != None:
        _set_numerical(node.right)


def _get_table(nodes):
    table = {}
    for node in nodes:
        table[node.data] = node.numeric
    return table