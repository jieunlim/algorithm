# 329. Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix):
        def helper(i, j):
            # print(f"i={i}, j={j}, memo={memo}")
            if memo[i][j] > 0:
                return memo[i][j]

            ret = 1
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if x >= 0 and x < len(matrix) \
                        and y >= 0 and y < len(matrix[0]) \
                        and matrix[x][y] > matrix[i][j]:
                    ret = max(ret, helper(x, y) + 1)

            memo[i][j] = ret
            return memo[i][j]

        if len(matrix) == 0: return 0

        memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if memo[i][j] == 0:
                    result = max(result, helper(i, j))

        return result


nums =[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

obj = Solution()
print(obj.longestIncreasingPath(nums))