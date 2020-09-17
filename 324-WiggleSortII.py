# 324. Wiggle Sort II

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# https://leetcode.com/problems/wiggle-sort-ii/discuss/155764/Python-3-lines-simplest-solution-for-everyone-to-understand

class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        print(f"arr={arr}")
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        print(f"nums={nums}")
        for i in range(0, len(nums), 2): nums[i] = arr.pop()
        print(f"nums={nums}")

nums=[3,5,2,1,6,4]
nums = [1, 5, 1, 1, 6, 4]
obj = Solution()
obj.wiggleSort(nums)
print(nums)

# 280. Wiggle Sort
# 376. Wiggle Subsequence