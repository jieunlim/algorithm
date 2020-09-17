# 200. Number of Islands
# Linear sacn the 2d grid map
# if node contains a '1', then the root node that triggers a Dpeth First Search.
# During DFS, every visited node should be set as '0' or visited mark.
# Count the number of root nodes that trigger DFS, this number would be the number of islands
# since DFS starting at some root identifies and island.
# time O(M*N), M columns, N rows
# space O(M*N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def helper(i, j):

            grid[i][j] = '#'
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == '1':
                        helper(x, y)

        if not grid: return 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    helper(i, j)
                    cnt += 1
        return cnt

    def numIslands2(self, grid):

        def dfs(i, j):
            print(f" dfs i={i}, j={j},visited={visited}")
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if not grid: return 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        print(f"r={r}, c={c}, visited={visited}")

        count = 0
        for i in range(r):
            for j in range(c):
                print(f" i={i}, j={j}, v={visited[i][j]}, g={grid[i][j]}")
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    print(f"   count={count}")
        return count

grid = [
['1', '1'],
['0', '0'],
['1', '1'] ]

obj = Solution()
print(obj.numIslands(grid))


grid = [
['1', '1', '1', '1', '0'],
['1', '1', '0', '1', '0'],
['1', '1', '0', '0', '0'],
['0', '0', '0', '0', '0']  ]


'''
class Solution:
    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True


    def numIslandsDFS(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc)


    def numIslandsBFS(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count


    def bfs(self, grid, r, c):
        queue = collections.deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'


'''