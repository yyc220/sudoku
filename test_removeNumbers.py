import unittest
from generate import generateSudoku,removeNumbers


def isValidSudoku(board):
    # 检查每一行是否合法
    for row in board:
        if not isValidRow(row):
            return False

    # 检查每一列是否合法
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not isValidRow(column):
            return False

    # 检查每个3x3的子区域是否合法
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if not isValidRow(subgrid):
                return False

    return True


def isValidRow(row):
    # 检查一行是否合法
    nums = set()
    for num in row:
        if num != 0 and num in nums:
            return False
        nums.add(num)
    return True

class TestSudoku(unittest.TestCase):
    def test_remove_numbers(self):
        # 创建一个数独棋盘
        board = generateSudoku()
        # 删除指定数量的数字
        count = 30
        removeNumbers(board, count)

        # 检查删除数字后的数独棋盘是否合法
        self.assertTrue(isValidSudoku(board))
        # 检查数独棋盘中的空白格数量是否等于指定删除的数量
        self.assertEqual(sum(row.count(0) for row in board), count)


if __name__ == '__main__':
    unittest.main()
