def sort(nodes):
    i = 1
    while nodes[-1].value > nodes[i].value or len(nodes) != i + 1:
        i += 1
    nodes[i], nodes[-1] = nodes[-1], nodes[i]