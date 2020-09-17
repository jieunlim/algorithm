# 79. Word Search

# time complexity: O(N*4^L)
# N is the number of cells in the board, L is the length of the word.
# 4-ary tree, 4 directions, 4^L
# space complexity: O(L), call stack would be the length of the word

class Solution(object):

    def exist11(self, board, word):

        def wordS(i, j, pos=0):
            print(f"[wordS]  i={i}, j={j}, pos={pos}")
            if pos == len(word):
                print(f"return True pos {pos} == len(word) {len(word)}, visited={visited}")
                return True

            # print(f" word[pos]={word[pos]}, board[i][j]={board[i][j]}")
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][
                j]:
                print(f"return False. visited={visited}")
                return False

            visited[(i, j)] = True
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                print(f"   for - rowOffset={rowOffset}, colOffset={colOffset}")
                res = wordS(i + rowOffset, j + colOffset, pos + 1)
                if res:
                    print(f" res={res}, break")
                    break
            visited[(i, j)] = False

            print(f"  endoffunc, i={i}, j={j}, return res - visited={visited}, res={res}")
            return res

        visited = {}
        print(f"board={board}, word={word}")
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(f"***i={i}, j={j}")
                if wordS(i, j):
                    return True

        return False




    # using visited hash data structure
    # DFS
    # https://leetcode.com/problems/word-search/discuss/27820/Python-DFS-solution
    def exist2(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True

        return False

    def getWords(self, board, word, i, j, visited, pos=0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
              or self.getWords(board, word, i, j - 1, visited, pos + 1) \
              or self.getWords(board, word, i + 1, j, visited, pos + 1) \
              or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res

    # https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/
    # backtracking
    # L: length of the word
    # N is the number of cells in the board
    # time O(N*4**L)
    # Space O(L)
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                print(f"row={row}, col={col}")
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):

        print(f"  backtrack row={row}, col={col}, suffix={suffix}")
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        print(f"  self.board={self.board}")
        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            print(f"return False")
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        print(f"  board={board}")
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            print(f"      for - row={row}, rowOffset={rowOffset}, col={col}, colOffset={colOffset}, suffix[1:]={suffix[1:]} ")
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            print(f"           ret={ret}")
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]
        print(f"  board={board},  suffix[0]={suffix[0]}, ret={ret}")

        # Tried all directions, and did not find any match
        return ret



    #
    # def exist2(self, board, word):
    #     if not board:
    #         return False
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if self.dfs(board, i, j, word):
    #                 return True
    #     return False
    #
    # # check whether can find word, start at (i,j) position
    # def dfs(self, board, i, j, word):
    #     if len(word) == 0:  # all the characters are checked
    #         return True
    #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
    #         return False
    #     tmp = board[i][j]  # first character is found, check the remaining part
    #     board[i][j] = "#"  # avoid visit agian
    #     # check whether can find "word" along one direction
    #     res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
    #           or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
    #     board[i][j] = tmp
    #     return res


##################
    # this code evaluates all of them no matter what
    # should return immediately once either up, down, left, right returns true
    # but easy to understand
    def exist3(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(f"i={i}, j={j}")
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        print(f"[dfs] board={board}, i={i}, j={j}, word={word}")
        if len(word) == 0:  # all the characters are checked
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        print(f"   word[0]={word[0]}, board[i][j]={board[i][j]}, tmp={tmp}")
        board[i][j] = "#"  # avoid visit agian
        print(f"   board={board} visited!")

        # check whether can find "word" along one direction
        print(f"     1. will call down {i+1}, {j}, {word[1:]}")
        down = self.dfs(board, i+1, j, word[1:])
        print(f"     2. down={down}  will call up {i-1}, {j}, {word[1:]}")
        up = self.dfs(board, i-1, j, word[1:])
        print(f"     3. up={up} will call right {i}, {j+1}, {word[1:]}")
        right = self.dfs(board, i, j+1, word[1:])
        print(f"     4. right={right}, will call left {i}, {j-1}, {word[1:]}")
        left = self.dfs(board, i, j-1, word[1:])
        print(f"         left={left}")
        board[i][j] = tmp
        print(f"        board={board}")
        return up or down or left or right


board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "CCED"

board=[["a","a"]]
word=["a"]

board=[
  ['B','C'],
  ['C','E']]

word = "CEC"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"  #True
obj = Solution()
print(obj.exist11(board, word))

# 489. Robot Room Cleaner.