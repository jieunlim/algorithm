
# 64. Minimum Path Sum
class Solution:
    # DP recursion
    # time complexity
    # space complexity
    def minPathSum(self, grid):
        MAX = float('inf')

        def minPS(i, j):
            print(f"i={i}, j={j}")

            if i >= len(grid) or j >= len(grid[0]):
                print(f"return MAX {MAX}")
                return MAX

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                print(f"return grid[i][j]={grid[i][j]}")
                return grid[i][j]

            if (i, j) in memo:
                print(f"return memo {memo[(i, j)]}")
                return memo[(i, j)]

            print(f" - ")
            memo[(i,j)] = min(minPS(i+1, j), minPS(i, j+1)) + grid[i][j]
            print(f" return memo[(i,j)] {memo[(i,j)]}, i={i}, j={j}, memo={memo}")
            return memo[(i,j)]

        memo = {}
        return minPS(0,0)

    # DP 1d
    # time O(mn), space O(n)
    def minPathSum2(self, grid):

        M, N = len(grid), len(grid[0])
        dp = [0] + [float('inf')] * (N - 1)

        print(f"dp={dp}")
        for i in range(M):
            dp[0] = dp[0] + grid[i][0]
            print(f"i={i}, dp={dp}")

            for j in range(1, N):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
                print(f" j={j}, dp={dp}")
        return dp[-1]

grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
obj = Solution()
print(obj.minPathSum(grid))

# 174. Dungeon Game
# 741. Cherry Pickup