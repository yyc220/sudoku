import random
import generate


def test_solveSudoku():
    # 构建一个已解决的数独谜题
    solution = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 6, 5, 8, 9, 7],
        [3, 6, 5, 8, 9, 7, 2, 1, 4],
        [8, 9, 7, 2, 1, 4, 3, 6, 5],
        [5, 3, 1, 6, 4, 2, 9, 7, 8],
        [6, 4, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 8, 5, 3, 1, 6, 4, 2]
    ]

    # 复制已解决的数独谜题，并移除一些数字
    board = [row[:] for row in solution]
    for _ in range(30):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    # 执行solveSudoku函数进行求解
    generate.solveSudoku(board)

    # 检查求解结果是否与预期一致
    assert board == solution
