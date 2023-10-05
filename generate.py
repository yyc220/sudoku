import random
import sys
import copy


def generateSudoku():
    # 初始化一个空的数独棋盘
    board = [[0] * 9 for _ in range(9)]

    # 使用回溯法填充数独棋盘
    solveSudoku(board)

    return board


def solveSudoku(board):
    # 查找空白位置
    row, col = findEmptyPosition(board)

    # 如果没有空白位置，表示数独已填满
    if row == -1 and col == -1:
        return True

    # 尝试填入数字
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if isValidMove(board, row, col, num):
            # 假设填入数字num
            board[row][col] = num

            # 递归填充剩余空白位置
            if solveSudoku(board):
                return True

            # 如果递归未成功，则撤销之前的假设
            board[row][col] = 0

    # 所有数字都尝试过但没有成功，返回False
    return False


def findEmptyPosition(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1


def isValidMove(board, row, col, num):
    # 检查行和列
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # 检查所在的子区域
    sub_row, sub_col = (row // 3) * 3, (col // 3) * 3
    for i in range(sub_row, sub_row + 3):
        for j in range(sub_col, sub_col + 3):
            if board[i][j] == num:
                return False

    return True


# 删除指定数量的数字
def removeNumbers(board, count):
    positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(positions)

    for pos in positions:
        row, col = pos
        temp = board[row][col]
        board[row][col] = 0

        # 检查数独是否有唯一解，若有则继续删除下一个格子，否则回复原值
        tempBoard = [row[:] for row in board]
        if not solveSudoku(tempBoard):
            board[row][col] = temp

        count -= 1
        if count == 0:
            break