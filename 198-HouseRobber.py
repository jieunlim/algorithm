

# 198. House Robber

# 붙어있는 집은 털 수 없으므로,
# i번 집을 포함한다면 한 집 건너 i+2 집으로 이동 nums[i] + F(i+2),
# 포함하지 않는다면 i+1 번째 집으로 이동 F(i+1)
# 이 두가지 중에 maximum을 구하면 되는 DP 문제

# time O(n), space O(n)
# Recursion
class Solution:
    def rob(self, nums):
        def robRe(i):
            if len(nums) <= i:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + robRe(i+2), robRe(i+1))
            return memo[i]
        memo = {}
        return robRe(0)

# time O(n), space O(1)
# Iteration
    def rob2(self, nums):

        prevM = curM = 0
        for n in nums:
            tmp = curM
            curM = max(curM, prevM + n)
            prevM = tmp
            # print(f"tmp={tmp}, curM={curM}, prevM={prevM}")
        return curM

nums=[1,2,3,1]
# nums=[2,7,9,3,1]
obj = Solution()
print(obj.rob(nums))
print(obj.rob2(nums))


# 256. Paint House
# 213. House Robber II
# 152. Maximum Product Subarray
# 276. Paint Fence
# 600. Non-negative Integers without Consecutive Ones
# 337. House Robber III
# 656. Coin Path
# 740. Delete and Earn


'''

# 198. House Robber
# time O(n), space O(n)
def rob(nums):
    def robRe(i):
        print(f"i={i}, memo={memo}")
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        memo[i] =  max(nums[i] + robRe(i+2), robRe(i+1))
        return memo[i]
    memo = {}
    return robRe(0)

# time O(n), space O(1)
def rob2(nums):
    prevMax = currMax = 0
    for n in nums:
        tmp = currMax
        currMax = max(prevMax + n, currMax)
        prevMax = tmp
        # print(f"currMax={currMax}, prevMax={prevMax}")

    return currMax

nums=[1,2,3,1]
# nums=[2,7,9,3,1]
print(rob(nums))
'''