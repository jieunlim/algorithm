
# 221. Maximal Square


class Solution:
    def maximalSquare(self, matrix):
        def helper(i, j):
            nonlocal rows, cols, memo

            if i >= rows or i < 0 or j >= cols or j < 0 or int(matrix[i][j]) != 1:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i,j)] = min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1)) + 1

            return memo[(i,j)]

        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        maxVal = 0
        for i in range(rows):
            for j in range(cols):
                if int(matrix[i][j]) == 1:
                    val = helper(i, j)
                    maxVal = max(maxVal, val)
        return maxVal ** 2


matrix = [
[1, 0, 1, 0, 0 ],
[1, 0, 1, 1, 1 ],
[1, 1, 1, 1, 0 ],
[1, 0, 0, 1, 0 ],
]
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
# matrix = [["0"]]
obj = Solution()
print(obj.maximalSquare(matrix))



# We define dp[i][j] the maximal ending at position (i, j).
# Thus, current state (dp[i][j])depends on left (dp[i][j - 1]),
# up (dp[i - 1][j]), and left-up's (dp[i - 1][j - 1]) states.
# The current state equals to the minimum of these three states
# plus matrix[i][j] because any smaller value will lead to a smaller square
# (holes in somewhere). I use maxArea to track the maximal square. When matrix[i][j] == '0',
# the maximal square ending at position (i, j) is obviously 0.
# Recurrence relation:
#
# For matrix[i][j] == 1, dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + int(matrix[i][j]).
#
# For matrix[i][j] == 0, dp[i][j] = 0

# https://leetcode.com/problems/maximal-square/discuss/61845/9-lines-Python-DP-solution-with-explaination
def maximalSquare(matrix):
    dp, maxArea = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
    print(f"dp={dp}, maxArea={maxArea}")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(f"* i={i}, j={j}, {matrix[i][j]}, {int(matrix[i][j]) == 1}")
            if i == 0 or j == 0:
                print(f"    ** i={i}, j={j} ")
                dp[i][j] = int(matrix[i][j])
            elif int(matrix[i][j]) == 1:
                print(f"    i={i}, j={j} ,{dp[i - 1][j - 1]}")
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            maxArea = max(maxArea, dp[i][j])
            print(f"maxAre={maxArea}, dp[i][j]={dp[i][j]}, dp={dp}")
    return maxArea*maxArea

matrix = [
[1, 0, 1, 0, 0 ],
[1, 0, 1, 1, 1 ],
[1, 1, 1, 1, 0 ],
[1, 0, 0, 1, 0 ],
]
# print(maximalSquare(matrix))