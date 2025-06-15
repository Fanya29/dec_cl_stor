def sort(nodes, node):
    i = 1
    while node.value > nodes[i].value:
        i += 1
    nodes.append(node)
    nodes[i], nodes[-1] = nodes[-1], nodes[i]
