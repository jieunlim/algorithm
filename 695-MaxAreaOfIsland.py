# 695. Max Area of Island

class Solution:

    # time O(r*c)
    # space O(1)
    def maxAreaOfIsland(self, grid):

        def dfs(i, j):
            # nonlocal cols, rows

            grid[i][j] = 2
            cnt = 1
            if i < rows - 1 and grid[i + 1][j] == 1:
                cnt += dfs(i + 1, j)
            if j < cols - 1 and grid[i][j + 1] == 1:
                cnt += dfs(i, j + 1)
            if i > 0 and grid[i - 1][j] == 1:
                cnt += dfs(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                cnt += dfs(i, j - 1)

            return cnt

        if not grid: return 0

        cols, rows = len(grid[0]), len(grid)
        maxCnt = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cnt = dfs(i, j)
                    maxCnt = max(maxCnt, cnt)

        return maxCnt

    def maxAreaOfIsland2(self, grid):
        def dfs(i, j):
            # nonlocal cols, rows

            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1 or (i, j) in visited:
                return 0

            visited.add((i, j))
            cnt = 1

            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                cnt += dfs(x, y)

            return cnt

        if not grid: return 0

        cols, rows = len(grid[0]), len(grid)
        visited = set()
        maxCnt = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cnt = dfs(i, j)
                    maxCnt = max(maxCnt, cnt)

        return maxCnt

grid = [[1,1]]
obj = Solution()
print(obj.maxAreaOfIsland(grid))