def dfs(matrix, node):
    stack = [node]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            for i, connected in enumerate(matrix[current]):
                if connected and i not in visited:
                    stack.append(i)
    return visited
