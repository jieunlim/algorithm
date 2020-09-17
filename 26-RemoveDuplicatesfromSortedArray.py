
# 26. Remove Duplicates from Sorted Array
# O(N), O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums: return 0

        dupIdx = 1
        for i in range(len(nums)):
            if nums[dupIdx - 1] != nums[i]:
                nums[dupIdx] = nums[i]
                dupIdx += 1
        return dupIdx

    def removeDuplicates2(self, nums):

        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


# i=2, j=4,
# [1,2,3,1,3]

nums = [1, 1, 2, 3, 3]
obj = Solution()
print(obj.removeDuplicates(nums))