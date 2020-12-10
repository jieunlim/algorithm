# 31. Next Permutation
#
# O(N)
# O(1)

# 3 steps
# 1234 -> 1243 ->1324 -> 1342 -> ...
# 1. from the end, find nums[i-1] > nums[i], i is a peak
#   if i == 0: reverse all
# 2. k = i-1, from the end, find nums[j] which is nums[k] < nums[j]
#   then, swap kth and jth
# 3. from k+1 to the end, reverse all
# 1243 -> k is 2, j is 3, swap 1342 -> reverse 4,2 then 1324

# 1,2,5,4,3
# 1 3 2 4 5
#
# 5,3,4,2,1
# 5 4 1 2 3

from typing import List
class Solution:
    def nextPermutation2(self, nums: List[int]) -> None:

        if not nums: return

        i = j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            return nums.reverse()

        while j > 0 and nums[i - 1] >= nums[j]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def nextPermutation(self, nums):

        i = j = len(nums) - 1

        # find peak
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return nums.reverse()

        # from the end, find a bigger value than the ith, then swap
        k = i-1
        while j >= 0 and nums[k] >= nums[j]:
            j -= 1
        print(f"i={i}, j={j}, k={k}")

        nums[k], nums[j] = nums[j], nums[k]

        # reverse the second part
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# i = 1, k = 0, j = 1 [5,1,1]

nums = [1,2,3]
nums=[1,2,4,3]
nums=[1,5,1]
nums=[5,1,1]
nums=[1,2,5,4,3]
obj = Solution()
obj.nextPermutation(nums)
print(nums)

# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3

# 1,2,4,3 -> 1, 3, 4,2 - 1,3,2,4


# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# Time O(N)
# Space O(1)

class Solution2(object):
    # https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.

    def nextPermutation2(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        print(f"i={i}")
        if i == 0:   # nums are in descending order
            nums.reverse()
            print(f"nums={nums}")
            return
        k = i - 1    # find the last "ascending" position
        print(f"i={i}, j={j}, k={k}")
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        print(f"nums={nums}")
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
            print(f"nums={nums}")

    def nextPermutation(self, nums):
        # find longest non-increasing suffix
        right = len(nums) - 1
        while nums[right] <= nums[right - 1] and right - 1 >= 0:
            right -= 1
        print(f"right={right}, nums={nums}")
        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)

        # find pivot
        pivot = right - 1
        successor = 0
        # find rightmost succesor
        for i in range(len(nums) - 1, pivot, -1):
            print(f"i={i}, nums[i]={nums[i]},nums[pivot]={nums[pivot]}")
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        print(f"successor={successor}")
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        print(f"nums[pivot]={nums[pivot]}, nums[successor]={nums[successor]}, nums={nums}")
        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)
        print(f"nums={nums}")

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# nums=[0, 1, 2, 5, 3, 3, 0]
# nums=[0, 1, 3, 0, 2, 3, 5]
# nums=[0, 1, 3, 0, 3, 5, 2]
# nums=[3,2,1]
# nums=[1,2,3]
# obj = Solution2()
# obj.nextPermutation(nums)
# print(nums)