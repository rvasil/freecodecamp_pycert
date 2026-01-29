def dfs(adj_matrix, node):
    cnt_nodes = len(adj_matrix)
    visited = []
    queue = [node]

    while queue:
        current = queue.pop()
        visited.append(current)
        for n in range(cnt_nodes):
            if n in visited:
                continue
            if adj_matrix[current][n] == 1:
                queue.append(n)
    return visited


nodes = dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
print(nodes)
