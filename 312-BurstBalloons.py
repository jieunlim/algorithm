# 312. Burst Balloons

class Solution:
    def maxCoin(self, nums, left, right):

        if len(nums) == 1:
            return nums[0]
        elif len(nums) < 1:
            return 0

        return self.maxCoin(nums)

    def maxCoins1(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]

        print(f"[maxCoins1] nums={nums}")
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        print(f" n={n}, dp={dp}")
        for k in range(2, n):
            print(f" [for] k={k}")
            for left in range(0, n - k):
                right = left + k
                print(f"     left={left}, right={right}")
                for i in range(left + 1, right):
                    print(f"        i={i}, dp[left][right]={dp[left][right]}")
                    print(f"         {nums[left]} * {nums[i]} * {nums[right]} + {dp[left][i]} + {dp[i][right]}")
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                    print(f"         dp[left][right]={dp[left][right]}")
                    print(f"         dp={dp}")
        return dp[0][n - 1]


    def maxCoins22(self, nums):
        from functools import lru_cache
        # @lru_cache(None)
        def mCoinsRe(left, right):

            print(f"-left={left}, right={right}")
            # no more balloons can be added
            if left + 1 == right: return 0

            if (left, right) in memo:
                print(f"return memo {memo[(left, right)]}")
                return memo[(left, right)]

            max_val = float('-inf')
            for i in range(left + 1, right):
                print(f"   [for] l={left},r={right}, i={i}, {nums[left]} * {nums[i]} * {nums[right]}")
                res = nums[left] * nums[i] * nums[right] + mCoinsRe(left, i) + mCoinsRe(i, right)
                print(f" res={res} left={left}, right={right}, i={i}")
                max_val = max(max_val, res)
                print(f"      max_val={max_val}")

            # add each balloon on the interval and return the maximum score
            print(f"** left={left}, right={right},  max_val={max_val}")
            memo[(left, right)] = max_val
            return memo[(left, right)]

        nums = [1] + nums + [1]
        print(f"nums={nums}")
        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        memo = {}
        return mCoinsRe(0, len(nums)-1)

    def maxCoins2(self, nums):
        from functools import lru_cache
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):

            # no more balloons can be added
            if left + 1 == right: return 0

            # add each balloon on the interval and return the maximum score
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)


nums = [3,2,5,8]
# nums = [3, 5]
obj = Solution()
print(obj.maxCoins22(nums))
# print(obj.maxCoins1(nums))