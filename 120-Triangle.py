# 120. Triangle

def minimumTotal(tri):
    def helper(i, j):
        nonlocal minSum
        if j > i or i >= len(triangle):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        minSum = min(helper(i+1, j), helper(i+1, j+1))

        memo[(i, j)] = minSum + triangle[i][j]
        return memo[(i, j)]

    minSum = 0
    memo = {}
    return helper(0,0)

tri=[[2],
     [3,4]]
print(minimumTotal(tri))