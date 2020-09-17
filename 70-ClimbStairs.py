
# 70. Climbing Stairs
# similar to Fibonacci
# F(n-1) + F(n-2) options to get n.
# if we get F(n-1), then F(n-1) options to get n
# from n-2 to get n, there are F(n-2) more ways to get n.
# time
# O(2^n) before memoization
# O(n), size of recursion tree can go upto n
# space O(n), the depth of recursion tree can go upto n

def climbStairs(n: int) -> int:
    def helper(idx):

        if idx == n:
            return 1
        elif idx > n:
            return 0

        if idx in memo:
            return memo[idx]

        memo[idx] = helper(idx + 1) + helper(idx + 2)

        return memo[idx]

    memo = {}
    return helper(0)

def climbStairs(n):

    def climbRe(i):
        if i <= 2:
            return i

        if i in memo:
            return memo[i]

        memo[i] = climbRe(i - 1) + climbRe(i - 2)

        return memo[i]

    memo = {}
    return climbRe(n)

    # def climbRe(i):
    #
    #     print(f"i={i}")
    #     if i > n:
    #         return 0
    #     if i == n:
    #         return 1
    #
    #     if i in memo:
    #         print(f"  memo i={i}, {memo}")
    #         return memo[i]
    #
    #     memo[i] = climbRe(i+1) + climbRe(i+2)
    #     print(f"   i={i} return {memo}")
    #     return memo[i]
    # memo = {}
    # return climbRe(0)

def climbStairs2(n):

    if n < 3:
        return n

    p1, p2, f = 1, 2, 0

    for i in range(3, n+1):
        f = p1+p2
        p1 = p2
        p2 = f

    return f

# def climbStairs(self, n):
#     a, b = 1, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# if you can jump 1 or 2 or 3 steps.
def climbStairs3(n):

    p = [0, 1, 2, 4]

    for i in range(4, n+1):
        p[i%4] = p[(i-1)%4] + p[(i-2)%4] + p[(i-3)%4]

    return p[n%4]
n=4
print(climbStairs2(n))
# print(climbStairs3(n))

# 509. Fibonacci Number
# 746. Min Cost Climbing Stairs
# 1137. N-th Tribonacci Number

# 344. Reverse String