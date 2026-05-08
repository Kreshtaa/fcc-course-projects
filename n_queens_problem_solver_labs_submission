def dfs_n_queens(n):
    if n < 1:
        return []
    solutions = []
    stack = [[]]

    def is_valid(placement, col):
        row = len(placement)
        for r, c in enumerate(placement):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True
    
    while stack:
        current = stack.pop(0)
        if len(current) == n:
            solutions.append(current)
        else:
            for col in range(n):
                if is_valid(current, col):
                    stack.append(current + [col])
    return solutions
