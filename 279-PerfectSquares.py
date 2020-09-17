# 279. Perfect Squares
# solution 1 - DP, memoization
# better solution - BFS로, sum - val 하면서 찾아가면, 먼저 0이 되는 level을 리턴,
#                   input array에 1 이 포함되는데, tree depth로 길어지므로 BFS 가 효율적인 접근 방법임.

# DP, memoization, subproblem DP[n]
# time O(sqrt(n))
# space O(n)

import math
class Solution:
    # BFS, level return
    def perfectSquare(self, n):
        from collections import deque
        # nums = []
        # for i in range(1, int(math.sqrt(n))+1):
        #     if i*i <= n:
        #         nums.append(i*i)
        # print(nums)

        nums = [i*i for i in range(1, int(math.sqrt(n))+1)]
        dq = deque([(n, 1)])

        while dq:
            value, level = dq.popleft()
            for num in nums[::-1]:
                if value - num == 0:
                    return level
                if value - num > 0:
                    dq.append((value - num, level+1))

        return -1

    # DP + memoization
    # time O(n*sqrt(n))
    # space O(n)
    def perfectSquare2(self, n):
        def helper(target):

            if target == 0: return 0
            if target in memo: return memo[target]

            minCnt = n
            for num in sqnums[::-1]:
                if target >= num:
                    cnt = helper(target-num) + 1
                    minCnt = min(minCnt, cnt)

            memo[target] = minCnt
            return memo[target]

        memo = {}
        sqnums = [ i*i for i in range(1, int(math.sqrt(n))+1) ]
        print(sqnums)
        return helper(n)

    def perfectSquare22(self, n):
        def helper(target):

            if target in sqnums: return 1
            if target in memo: return memo[target]

            minCnt = n
            for num in sqnums[::-1]:
                if target > num:
                    cnt = helper(target-num) + 1
                    minCnt = min(minCnt, cnt)

            memo[target] = minCnt
            return memo[target]

        memo = {}
        sqnums = [ i*i for i in range(1, int(math.sqrt(n))+1) ]
        print(sqnums)
        return helper(n)

    def perfectSquare3(self, n):
        def helper(target):
            # print(f"target = {target}, memo={memo}")
            if target in sqNum: return 1

            if target in memo:
                return memo[target]

            minN = float('inf')
            for s in sqNum:
                # print(f"  for s={s}, target={target}")
                if s > target:
                    # print(f"    break")
                    break
                rtnN = helper(target - s) + 1
                minN = min(minN, rtnN)
                # print(f"rtnN={rtnN}, minN={minN}, target={target}")
                memo[target] = minN

            return memo[target]

        sqNum = [i*i for i in range(1, int(math.sqrt(n)+1))]
        # print(f"sqNum={sqNum}, n={n}")
        memo = {}
        return helper(n)

# n=13
# # n=8
# print(perfectSquare(n))
n = 500
n=12
obj = Solution()
print(obj.perfectSquare2(n))



'''
    def numSquares3(self, n):
    
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
    
        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0
    
        print(square_nums, dp)
    
        for i in range(1, n + 1):
            print(f"i={i}")
            for square in square_nums:
                print(f"  square={square}, dp[{i}]={dp[i]}")
                if i < square:
                    print(f"    break")
                    break
                print(f"    dp[{i}]={dp[i]}, dp[i - square] + 1={dp[i - square] + 1}")
                dp[i] = min(dp[i], dp[i - square] + 1)
                print(f"    dp={dp}")
    
        return dp[-1]

n=12
n=5
# print(numSquares2(n))
'''