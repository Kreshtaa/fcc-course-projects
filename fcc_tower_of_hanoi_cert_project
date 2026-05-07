def hanoi_solver(n):
    rod_1 = list(range(n, 0, -1))
    rod_2 = []
    rod_3 = []

    def state():
        return f"{rod_1} {rod_2} {rod_3}"
    progress = [state()]

    def move(n, source, target, auxiliary):
        if n == 1:
            target.append(source.pop())
            progress.append(state())
        else:
            move(n - 1, source, auxiliary, target)
            target.append(source.pop())
            progress.append(state())
            move(n - 1, auxiliary, target, source)
    
    move(n, rod_1, rod_3, rod_2)
    return '\n'.join(progress)
