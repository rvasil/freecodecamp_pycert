#
# You can move only top-most disks.
# You can move only one disk at a time.
# You cannot place larger disks on top of smaller ones.

# hanoi_solver function should solve the puzzle following the given rules in 2n - 1 moves, where n is the total number of disks.

# hanoi_solver(2) should return
# [2, 1] [] []
# [2] [1] []
# [] [1] [2]
# [] [] [2, 1]

# hanoi_solver(3) should return
# [3, 2, 1] [] []
# [3, 2] [] [1]
# [3] [2] [1]
# [3] [2, 1] []
# [] [2, 1] [3]
# [1] [2] [3]
# [1] [] [3, 2]
# [] [] [3, 2, 1]

# hanoi_solver(4) should return
# [4, 3, 2, 1] [] []
# [4, 3, 2] [1] []
# [4, 3] [1] [2]
# [4, 3] [] [2, 1]
# [4] [3] [2, 1]
# [4, 1] [3] [2]
# [4, 1] [3, 2] []
# [4] [3, 2, 1] []
# [] [3, 2, 1] [4]
# [] [3, 2] [4, 1]
# [2] [3] [4, 1]
# [2, 1] [3] [4]
# [2, 1] [] [4, 3]
# [2] [1] [4, 3]
# [] [1] [4, 3, 2]
# [] [] [4, 3, 2, 1]


def status(rods: dict) -> str:
    return " ".join([str(r) for r in rods.values()])


def move(src: list, to: list):
    to.append(src.pop())


def solve_hanoi(n, rods, source, dest, via) -> list:
    solve_steps = []
    if n == 1:
        move(rods[source], rods[dest])
        solve_steps += [status(rods)]
    else:
        solve_steps.extend(solve_hanoi(n - 1, rods, source, via, dest))
        move(rods[source], rods[dest])
        solve_steps += [status(rods)]
        solve_steps.extend(solve_hanoi(n - 1, rods, via, dest, source))
    return solve_steps


def hanoi_solver(n: int) -> str:
    initial = list(range(n, 0, -1))
    rods = {"A": initial.copy(), "B": [], "C": []}
    steps = [status(rods)]
    steps.extend(solve_hanoi(n, rods, "A", "C", "B"))  # A to C using B
    assert initial == rods["C"]
    return "\n".join(steps)


if __name__ == "__main__":
    print(hanoi_solver(2))
    print("-" * 90)
    print(hanoi_solver(3))
    print("-" * 90)
    print(hanoi_solver(4))
