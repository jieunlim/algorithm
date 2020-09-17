# 62. Unique Paths

def uniquePath(m, n):

    def P(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if i == m-1 and j == n - 1:
            return 1

        if (i,j) in memo:
            return memo[(i,j)]

        memo[(i,j)] = P(i + 1, j) + P(i, j + 1)
        return memo[(i,j)]

    memo = {}
    return P(0,0)

m=3
n=2

m=7
n=3

print(uniquePath(m, n))
