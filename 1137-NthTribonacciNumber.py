# 1137. N-th Tribonacci Number
# time O(N)
# space O(1)
def tribonacci(n):

    p = [0, 1, 1, 0]
    for i in range(3, n+1):
        p[i%4] = p[(i-1)%4] + p[(i-2)%4] + p[(i-3)%4]
    print(p)
    return p[n%4]

def tribonacci2(n):

    p = [0, 1, 1]
    f = 0
    if n < 3:
        return p[n]

    for i in range(3, n+1):
        f = p[0]+ p[1]+ p[2]
        p[0] = p[1]
        p[1] = p[2]
        p[2] = f
        print(f"p={p}, f={f}")
    return f


def tribonacci3(n):
    def tri(n):
        p = [0, 1, 1, 2]
        if n < 4:
            return p[n]

        if n in memo:
            return memo[n]
        memo[n] = tri(n - 1) + tri(n - 2) + tri(n - 3)
        return memo[n]

    memo = {}
    return tri(n)
n=5
print(tribonacci3(n))