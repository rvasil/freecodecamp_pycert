# lab-n-queens-problem
#
# The N-Queens problem asks you to place N queens on an N×N chessboard
# so that no two queens attack each other (no two share a row, column, or diagonal).
#
# User Stories:

# - You should have a function named dfs_n_queens.
# - The function should accept exactly one argument: an integer n.
# - If n is less than 1, the function should return an empty list ([]).
# - The function should return a list of solutions; each solution is itself a list of length n, where the element at index i is the column index (0-based) of the queen in row i.


def diagonals_allow(current: list, nextindex: int) -> bool:
    """Check if existing diagonals allow placing a queen at `nextindex` row in next column."""
    for r in range(1, len(current) + 1, 1):
        if abs(nextindex - current[-r]) == r:
            return False
    return True


def backtrack_n_queens(matrix_size: int, options: list, current: list, solutions: list):
    if len(current) == matrix_size:
        print(f"solution #{len(solutions) + 1}: {current}")
        solutions.append(current.copy())
        return

    for x in options:
        # x not in current - this is guaranteed by options removal for `next_options`
        if diagonals_allow(current, x):
            current.append(x)
            next_options = options.copy()
            next_options.remove(x)
            backtrack_n_queens(matrix_size, next_options, current, solutions)
            current.pop()  # return to previous state


def dfs_n_queens(n: int):
    """
    Depth-First Search solution to the N-Queens problem on an N×N chessboard.

    :param n: size of the chessboard and number of queens
    :type n: int
    """

    solutions = []
    current = []

    if n < 1:
        print(f"n must be at least 1, got {n}")
        return solutions

    print(f"-----------------Running for matrix of size {n=}-----------------")

    options = list(range(n))
    backtrack_n_queens(n, options, current, solutions)
    return solutions


def main():
    assert dfs_n_queens(1) == [[0]]
    assert dfs_n_queens(2) == []
    assert dfs_n_queens(3) == []
    for n in [4, 5]:
        result = dfs_n_queens(n)
        out = (result) if n < 5 else "..."
        print("========== returning: ", n, len(result), out)

    assert len(dfs_n_queens(4)) == 2
    assert len(dfs_n_queens(5)) == 10


if __name__ == "__main__":
    main()
