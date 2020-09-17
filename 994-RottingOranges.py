
# 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid):
        import collections

        n,m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        print(f"cnt={cnt}, Q={Q}")
        res = 0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                print(f"i={i}, j={j}")
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    print(f"    x={x}, y={y}")
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
                        print(f"    q = {Q}, grid={grid}, cnt={cnt}")
                print(f"len(Q)={len(Q)}")
            res += 1
            print(f"res={res}")
        return max(0, res-1) if cnt == 0 else -1

    # time O(N) - N is the size of the grid
    # space O(N)
    def orangesRotting2(self, grid):
        from collections import deque

        myQ = deque()
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
                if grid[i][j] == 2:
                    myQ.append((i, j, 0))
        time = 0
        while len(myQ) > 0:
            i, j, time = myQ.popleft()
            # print(f"i={i}, j={j}, time={time}")
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                # print(f"x={x}, y={y}, grid[x][y]={grid[x][y]}")
                if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                    if grid[x][y] == 1:
                        myQ.append((x, y, time + 1))
                        grid[x][y] = 2
                        cnt -= 1

        return time if cnt == 0 else -1

grid = [[2,1,1], [1,1,0], [0,1,1]]
obj = Solution()
print(obj.orangesRotting2(grid))