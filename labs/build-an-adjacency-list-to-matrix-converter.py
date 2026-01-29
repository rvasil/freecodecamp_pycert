def adjacency_list_to_matrix(adj_dict: dict):
    nodes = adj_dict.keys()
    adj_matrix = [[0 for _ in nodes] for _ in nodes]
    for node, adjs in adj_dict.items():
        for adj in adjs:
            adj_matrix[node][adj] = 1

    for r in adj_matrix:
        print(r)
    return adj_matrix


adj_list = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}

adjacency_list_to_matrix(adj_list)
