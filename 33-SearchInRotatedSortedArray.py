# 33. Search in Rotated Sorted Array

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    def search2(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if target < nums[0] < nums[mid]:  # -inf
               start = mid + 1
            elif target >= nums[0] > nums[mid]:  # +inf
                end = mid
            elif nums[mid] < target:
               start = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        return -1

nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
print(obj.search2(nums, target))