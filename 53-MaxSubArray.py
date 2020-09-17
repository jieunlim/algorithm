
# 53. Maximum Subarray
from typing import List
# O(N), O(1)
# maxSofar - max sum seen so far
# maxSub - current max sum
def maxSubArray(nums):

    if len(nums) < 2:
        return nums

    maxSofar = maxSub = nums[0]

    # for n in nums[1:]:
    #     maxSub = max(n, maxSub+n)
    for i in range(1, len(nums)):
        maxSub = max(nums[i], maxSub+nums[i])
        maxSofar = max(maxSub, maxSofar)

    return maxSofar

nums=[-2,1,-3,4,-1,2,1,-5,4]
nums = [2,-3,4,-8,0]
# nums=[]
# nums=[1]
# print(maxSubArray(nums))
# print(obj.maxSubArray(nums))


# 53. Maximum Subarray
# find the contiguous subarray
# return its largest sum
# i번째 element에서, 이전까지 sum을 합할지,의 아니 i번째부터 다시 array를 시작할지면를 결정.
# (i번째 값)과, (i번째 값 + 이전까지의 합) 둘  최대값을 curSum
# -2, 1,-3, 4 의 경우
# curSum은 -2, 1(-2는 버림), -2(1+(-3)), 4(이전 값 선택 안하고 4에서 새로 subarray시작)
# 반복문 내에서 지금까지의 최대값을 maxSum 으로 저장해서 maxSum 리턴

class Solution2:
    def maxSubArray(self, nums):

        if not nums: return
        elif len(nums) == 1: return nums[0]

        curSum = maxSum = nums[0]

        for n in nums[1:]:
            curSum = max(n, curSum+n)
            maxSum = max(maxSum, curSum)

        return maxSum


    def maxSubArray(self, nums: List[int]) -> int:
        # 1 line solution
        # return max(itertools.accumulate(nums, lambda x,y: x+y if x > 0 else y ))

        # Greedy: Compute CumSum while tracking MaxCumSum so far, but reset CumSum if previous CumSum < 0.
        max_sum = nums[0]
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums > max_sum:
                max_sum = sums
            if sums < 0:
                sums = 0
        return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
# nums=[]
# nums=[1]
# nums=[-2,0,-1]
# nums=[2,3,-2,4]
obj = Solution2()
print(obj.maxSubArray(nums))

# recursive
def maxSub21(arr):
    def helper(i, j ):
        if i > j:
            return 0

        if (i,j) in memo:
            return memo[(i,j)]

        print(f"i={i}, j={j}, arr[i] = {arr[i]}")
        rtn = max(helper(i+1, j) + arr[i], arr[i])
        print(f"rtn = {rtn}")
        memo[(i,j)] = rtn

        return rtn

    memo = {}
    rtn = helper(0, len(arr)-1 )
    print(f"rtn={rtn}, memo={memo}")
    return max(memo.values())


def maxSubArray(nums: List[int]) -> int:
    def helper(i):
        nonlocal maxVal
        if i >= len(nums):
            return 0

        print(f"i={i}")
        if i in memo:
            print(memo)
            return memo[i]

        memo[i] = max(helper(i + 1) + nums[i], nums[i])
        if maxVal < memo[i]: maxVal = memo[i]

        return memo[i]

    maxVal = float('-inf')
    memo = {}
    rtn = helper(0)
    return maxVal

print("+++++")
arr = [-2,1,-3,4,-1,2,1,-5,4]
# arr=[-1,-2,3]
print(maxSubArray(arr))
