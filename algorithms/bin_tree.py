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