
# 213. House Robber II

# 198. House Robber과 동일한데, 첫번째와 마지막 집이 연결되어 있어서, 첫번째 집을 터는 경우 마지막 집을 털 수 없음.
# 입력 array인 nums의 첫번째 집을 빼고 최대값을 구하고,
# 마지막 집을 빼고 최대값을 구한 후
# 두 값의 maximum을 구하면 되는 DP 문제

class Solution(object):
# time O(n), space O(1)
    def rob(self, nums):
        def robii(num):
            prevM = curM = 0
            for n in num:
                tmpM = curM
                curM = max(prevM + n, curM)
                prevM = tmpM
            return curM
        if not nums: return 0
        elif len(nums) == 1: return nums[0]

        return max(robii(nums[1:]), robii(nums[:-1]))

# time O(n), space O(n)
    def rob22(self, nums: List[int]) -> int:
        def helper(idx, length):
            if idx >= length:
                return 0
            if idx in memo:
                return memo[idx]
            memo[idx] = max(helper(idx + 2, length) + nums[idx], helper(idx + 1, length))
            return memo[idx]

        if not nums:
            return 0
        elif len(nums) < 2:
            return nums[0]

        memo = {}
        r1 = helper(1, len(nums))
        memo = {}
        r2 = helper(0, len(nums) - 1)
        return max(r1, r2)

    def rob2(self, nums):
        def robRe(num, i):
            if len(num) <= i:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(num[i] + robRe(num, i+2), robRe(num, i+1))
            return memo[i]

        if not nums: return 0
        elif len(nums) == 1: return nums[0]

        memo = {}
        rtn1 = robRe(nums[1:], 0)
        memo = {}
        rtn2 = robRe(nums[:-1], 0)
        return max(rtn1, rtn2)

nums = [2,3,2]
obj = Solution()
print(obj.rob(nums))
print(obj.rob2(nums))
