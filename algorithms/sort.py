def sort(nodes):
    for i in range(len(nodes) - 1, 0, -1):
        if nodes[i].value >= nodes[i - 1].value:
            break
        nodes[i], nodes[i-1] = nodes[i-1], nodes[i]
