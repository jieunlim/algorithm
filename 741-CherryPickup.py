# 741. Cherry Pickup
class Solution(object):
    def cherryPickup(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        print(f"dp = {dp}")

        for t in range(1, 2*N - 1):
            dp2 = [[float('-inf')] * N for _ in range(N)]
            print(f"t={t}, dp2={dp2}")
            for i in range(max(0, t-(N-1)), min(N-1, t) + 1):
                for j in range(max(0, t-(N-1)), min(N-1, t) + 1):
                    print(f"i={i}, j={j}")
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        print(f"continue")
                        continue

                    val = grid[i][t-i]
                    if i != j: val += grid[j][t-j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i-1, i) for pj in (j-1, j)
                                    if pi >= 0 and pj >= 0)
                    print(f"val={val}, dp2={dp2}")
            dp = dp2
        return max(0, dp[N-1][N-1])


class Solution2(object):
    def __init__(self):
        self.count = 0

    def cherryPickup(self, grid):
        if grid[-1][-1] == -1: return 0
        self.grid = grid
        self.memo = {}
        self.N = len(grid)

        ans = max(self.dp(0, 0, 0, 0), 0)
        print
        self.count
        return ans

    def dp(self, i1, j1, i2, j2):
        self.count += 1
        if (i1, j1, i2, j2) in self.memo: return self.memo[(i1, j1, i2, j2)]
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N - 1 and j1 == N - 1 and i2 == N - 1 and j2 == N - 1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1

        dd = self.dp(i1 + 1, j1, i2 + 1, j2)
        dr = self.dp(i1 + 1, j1, i2, j2 + 1)
        rd = self.dp(i1, j1 + 1, i2 + 1, j2)
        rr = self.dp(i1, j1 + 1, i2, j2 + 1)
        maxComb = max([dd, dr, rd, rr])

        if maxComb == -1:
            out = -1
        else:
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]

        self.memo[(i1, j1, i2, j2)] = out
        return out
grid = [[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
obj = Solution2()
print(obj.cherryPickup(grid))