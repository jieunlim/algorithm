 # 200. Number of Islands

class Solution:
    def numIslands(self, grid):

        def dfs(i, j):
            print(f" dfs i={i}, j={j}, grid={grid}, visited={visited}")
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