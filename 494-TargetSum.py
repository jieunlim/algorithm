# 494. Target Sum

from collections import defaultdict
class Solution(object):

    def findTargetSumWays(self, nums, S):
        if not nums: return 0
        memo = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        # memo = {0:1}
        for n in nums[1:]:
            tMemo = defaultdict(int)
            print(f"memo={memo}")
            for key, cnt in memo.items():
                tMemo[key+n] += cnt
                tMemo[key-n] += cnt
            memo = tMemo
        return memo[S]


    # O(2^n) without memoization
    # O(n*l) with memoization, l refers to the range of sum, n refers to the size of nums
    # space O(n)
    # https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.

    def findTargetSumWays2(self, nums, S):
        def helper(i, curSum):
            print(memo)
            if i == len(nums):
                if curSum == S:
                    return 1
                else:
                    return 0

            if (i, curSum) in memo:
                return memo[(i, curSum)]

            print(f"i={i}, nums[i]={nums[i]}, curSum={curSum}")
            count = helper(i+1, curSum+nums[i])
            count += helper(i+1, curSum-nums[i])

            memo[(i, curSum)] = count
            return memo[(i, curSum)]

        if not nums:
            return 0

        memo = {}
        return helper(0, 0)

    def findTargetSumWays3(self, nums, S):
        dp = [{} for _ in range(len(nums))]

        if nums[0] == 0:
            dp[0] = {0 : 2}
        else:
            dp[0] = {nums[0] : 1, -nums[0] : 1}

        for i in range(1, len(nums)):
            curr_hist = {}
            for k, v in dp[i-1].items():
                    curr_hist[k+nums[i]] = curr_hist.get(k+nums[i], 0) + v
                    curr_hist[k-nums[i]] = curr_hist.get(k-nums[i], 0) + v
            dp[i] = curr_hist

        return dp[-1].get(S, 0)

nums=[1, 1, 1, 1, 1]
S=3
# nums=[1,2,3]
# S=4
nums=[0,38,42,31,13,10,11,12,44,16,38,17,22,28,9,27,20,35,34,39]
S=2
obj = Solution()
print(obj.findTargetSumWays2(nums, S))

'''
    def findTargetSumWays(self, nums, S):
        memo = {0: 1}
        print(f"nums={nums}, S={S}")
        for x in nums:
            m = defaultdict(int)
            print(f"x={x}, m={m}, memo={memo}")
            for key, cnt in memo.items():
                m[key + x] += cnt
                m[key - x] += cnt
                print(f"  key={key}, cnt={cnt}, m={m}")
            memo = m
        return memo[S]

'''

'''

    def findTargetSumWays3(self, nums, S):
        print(f"nums={nums}, S={S}")
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        print(f"dic={dic}")

        for i in range(1, len(nums)):
            print(f"i={i}")
            tdic = {}
            for d in dic:
                print(f"    d={d}")
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
                print(f"    tdic={tdic}")
            dic = tdic
            print(f"dic={dic} ")
        return dic.get(S, 0)
'''