
# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:


    #   2,3,1,2,4,3
    #   2 5 6 8
    # i=0 ,j=3    (4)
    # i=1,  8-[i] = 6,
    #     +[j] j=4   10 (j-i = 3)

    if not nums: return 0

    i, j, subSum, minSize = 0, 0, nums[0], float('inf')

    while i < len(nums) and j < len(nums):

        if subSum < s:
            j += 1
            if j < len(nums): subSum += nums[j]
        else:
            minSize = min(minSize, j - i + 1)

            subSum -= nums[i]
            i += 1

    return minSize if minSize != float('inf') else 0

    # s = 3
    # [1,2]
    # subSum = 3
    # i=0, j=1