import random
import sys
import copy


# 交换两行
def swapRows(board, row1, row2):
    if 0 <= row1 < 9 and 0 <= row2 < 9:
        board[row1], board[row2] = board[row2], board[row1]


# 交换两列
def swapColumns(board, col1, col2):
    if 0 <= col1 < 9 and 0 <= col2 < 9:
        for i in range(9):
            temp = board[i][col1]
            board[i][col1] = board[i][col2]
            board[i][col2] = temp


# 打乱数独面板
def shuffleBoard(board):
    for i in range(9):
        r1 = random.randint(0, 2)
        r2 = random.randint(0, 2)
        swapRows(board, i * 3 + r1, i * 3 + r2)

    for i in range(9):
        c1 = random.randint(0, 2)
        c2 = random.randint(0, 2)
        swapColumns(board, i * 3 + c1, i * 3 + c2)


# 检查移动是否合法
def isValidMove(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False

    return True


# 查找空单元格
def findEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] is None:
                return {
                    "row": i,
                    "col": j
                }
    return None


# 用回溯法解答数独
def solveSudoku(board):
    emptyCell = findEmptyCell(board)

    if not emptyCell:
        return True

    row = emptyCell["row"]
    col = emptyCell["col"]

    for num in range(1, 10):
        if isValidMove(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board):
                return True

            board[row][col] = None

    return False


# 判断数独是否有唯一解
def hasUniqueSolution(board):
    copy_board = copy.deepcopy(board)
    return solveSudoku(copy_board) and isBoardFilled(copy_board)


# 判断数独面板是否已填满
def isBoardFilled(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] is None:
                return False

    return True


# 删除指定数量的数字
def removeNumbers(board, count):
    cells = []

    for i in range(9):
        for j in range(9):
            cells.append({
                "row": i,
                "col": j,
            })

    while count > 0 and len(cells) > 0:
        index = random.randint(0, len(cells) - 1)
        cell = cells.pop(index)
        row = cell["row"]
        col = cell["col"]

        num = board[row][col]
        board[row][col] = 0

        copy_board = copy.deepcopy(board)
        solutionCount = 0

        solveSudoku(copy_board)

        if hasUniqueSolution(copy_board):
            count -= 1
        else:
            board[row][col] = num


def generateBoards():
    currentBoard = [[None] * 9 for _ in range(9)]
    solveSudoku(currentBoard)
    shuffleBoard(currentBoard)
    return currentBoard
