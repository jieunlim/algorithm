# 289. Game of Life
# https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
# time O(M*N), space O(1)
# 1 -> 0 (2)
# 0-> 1 (-1)
class Solution:
    def gameOfLife(self, board):

        if not board: return

        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                neighbors = 0
                if i > 0 and j > 0 and (board[i-1][j-1]&1) == 1: neighbors += 1
                if i > 0 and (board[i-1][j]&1) == 1: neighbors += 1
                if j > 0 and (board[i][j-1]&1) == 1: neighbors += 1
                if i < rows-1 and j > 0 and (board[i+1][j-1]&1) == 1: neighbors += 1
                if i > 0 and j < cols-1 and (board[i-1][j+1]&1) == 1: neighbors += 1
                if i < rows - 1 and (board[i+1][j]&1) == 1: neighbors += 1
                if j < cols - 1 and (board[i][j+1]&1) == 1: neighbors += 1
                if i < rows - 1 and j < cols - 1 and (board[i+1][j+1]&1) == 1: neighbors += 1

                if board[i][j] == 1 and neighbors == 2:
                    board[i][j] += 2
                elif neighbors == 3:
                    board[i][j] += 2

        for i in range(rows):
            for j in range(cols):
                board[i][j] = board[i][j] >> 1


    def gameOfLife2(self, board):

        def getCnt(i, j):
            cntOne = 0
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1),
                         (i - 1, j + 1)]:
                if x >= 0 and x < rows and y >= 0 and y < cols and board[x][y] in [1,2] :
                    cntOne += 1

            return cntOne

        def helper(i, j):
            cntOne = getCnt(i, j)

            if board[i][j] == 1:
                if cntOne < 2 or cntOne > 3:
                    board[i][j] = 2
                # elif cntOne == 2 or cntOne == 3:
                #     board[i][j] = 1
            else:
                if cntOne == 3:
                    board[i][j] = -1

        if not board: return None
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                helper(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

# import copy
# def gameOfLife(board):
#
#     r = len(board)
#     c = len(board[0])
#
#     neighbors = [(1,0), (0,1), (-1,0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
#     copyBoard = copy.deepcopy(board)
#
#     print(f"copyBoard={copyBoard}")
#     for i in range(r):
#         for j in range(c):
#             neiCnt = 0
#             print(f"i={i}, j={j}")
#             for nei in neighbors:
#                 row = i + nei[0]
#                 col = j + nei[1]
#
#                 print(f"   row={row}, col={col}, {copyBoard[i][j]}")
#                 if (row >= 0 and row < r) and (col >= 0 and col < c) and copyBoard[row][col] == 1:
#                     neiCnt += 1
#             print(f"neiCnt={neiCnt}")
#             if copyBoard[i][j] == 1 and (neiCnt < 2 or neiCnt > 3):
#                 board[i][j] = 0
#             if copyBoard[i][j] == 0 and neiCnt == 3:
#                 board[i][j] = 1

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

obj = Solution()
obj.gameOfLife(board)
print(board)

from typing import List
class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        print(f"copy_board={copy_board}")
        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:
                    print(f"row={row}, col={col}, neighbor={neighbor}")

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    print(f"r={r}, c={c}")
                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1
                        print(f"live_neighbors={live_neighbors}")

                # Rule 1 or Rule 3
                print(f"copy_board={copy_board}")
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                    print(f"(Rule 1 or Rule 3) board={board}")
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
                    print(f"(Rule 4) board={board}")
# board = [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
#
# obj = Solution()
# print(obj.gameOfLife(board))
# print(board)
