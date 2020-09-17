# 153. Find Minimum in Rotated Sorted Array
# an array sorted in ascending order is rotated at some pivot
# Find the minimum element.


# Binary Search
# Since the given array is sorted, we can make use of binary search.
# However, the array is rotated. So simply applying the binary search won't work here
# if the array is not rotated and the array is in ascending order, then last element > first element.
# 2,3,4,5,6,7  =>   2 < 7 means sorted, no rotation
# 4,5,6,7,2,3  =>   4 > 3, the first element is greater than the last, means rotated.
# between 7, 2 is the Inflection point


class Solution:
    def findMin(self, nums):
        if not nums: return

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2

            if  nums[start] <= nums[end]:
                return nums[start]
            elif nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid

        return nums[start]


nums=[4,5,6,7,2,3]
nums=[3,4,5,1,2]
# nums=[1,2,-3]
obj = Solution()
print(obj.findMin(nums))