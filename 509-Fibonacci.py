# leetcode 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N)

##########################################################
# (1) DP - bottom up using three variables
# time-O(N), space O(1)
def fibonacci(N):
    p1 = 0
    p2 = 1
    f = 0

    if N <= 1:
        return N

    for i in range(2,N+1):
        f = p1+p2
        p1 = p2
        p2 = f

    return f

N=5
for i in range(N+1):
    print( f"fibonacci({i}) = {fibonacci(i)}" )

##########################################################
# (2) DP- bottom up using array
# time O(N), space O(N)
def fib_botton_array(N):

    #Array to store fib numbers
    arr = [0 for _ in range(N+1)]

    arr[0] = 0
    arr[1] = 1

    for i in range(2, N+1):
        #compute fib_botton_array(N) and store it
        arr[i] = arr[i-1]+arr[i-2]

    return arr[N]

N=5
print("fib_botton_array=", fib_botton_array(N))

##########################################################
# (5) recursion(Top down) + memoization
# time-O(N), space-O(N) dictionary
def fib_topdown(N):

    if N <= 1:
        return N

    if N in memo:
        return memo[N]

    memo[N] = fib_topdown(N-1) + fib_topdown(N-2)
    return memo[N]

memo = {}
print(f"fib_topdown ({N})={fib_topdown(N)}")
print(memo)

##########################################################
# (6) using n array
# time-O(N), space-O(1) using 3 array
# previous n 개에 대해서 풀때 활용 가능
def fib_3array(N):
    p = [0, 1, 0]

    for i in range(2, N+1):
        p[i % 3] = p[(i - 1) % 3] + p[(i - 2) % 3]
        # print(p)

    return p[N % 3]

N=5
print(f"fib_3array({N}) = {fib_3array(N)}")


#
def fib_4(N):
    p = [0, 1, 1, 0]

    for i in range(3, N + 1):
        p[i % 4] = p[(i - 1) % 4] + p[(i - 2) % 4] + p[(i - 3) % 4]

    return p[N % 4]







##########################################################
# (3) DP- bottom up using dictionary
# time O(N), space O(N)
# leetcode - Approach 2: Bottom-Up Approach using Memoization
# 0 부터 ( f(N)을 구하기 위해 트리의 맨 아래 f(0) 부터 구해서 올라감 )

def fib_bottom_dict(N: int) -> int:
    def memoize(N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
            print(cache)

        return cache[N]

    if N <= 1:
        return N
    return memoize(N)


N=5
print("fib_bottom_dict=", fib_bottom_dict(N))

##########################################################
# (4) recursion
# recursion 개념 이해를 위해서만 사용
# exponentialtime-O(2**N), space-O(N)
def fib_recursion(N):

    if N <= 1:
        return N

    return fib_recursion(N-1) + fib_recursion(N-2)

N=5
print("fib_recursion : ", fib_recursion(N))
