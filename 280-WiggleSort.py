
# 280. Wiggle Sort

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# sorting O(nlogn) and swap
# space O(1)

class Solution(object):

    def wiggleSort(self, nums):

        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

    def wiggleSort2(self, nums):

        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        for i in range(0, len(nums), 2): nums[i] = arr.pop()

        # for i in range(1, len(nums)):
        #     if (i % 2) ^ (nums[i] > nums[i - 1]):
        #         print(f"i={i}, nums={nums}")
        #         nums[i], nums[i - 1] = nums[i - 1], nums[i]
        #         print(f"    nums={nums}")

    def wiggleSort3(self, a):
        if not a:
            return
        n = len(a)
        for i in range(1, n, 2):
            print(f"{a[i - 1]}, {a[i]}, a={a}")
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

            # if i + 1 < n: print(f"  {a[i]}, {a[i + 1]}, a={a}")
            if i + 1 < n and a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

nums=[3,5,2,1,6,4]
nums=[7,6,6,9]
nums=[1,7,4,9,2,5]
obj = Solution()
obj.wiggleSort(nums)
print(nums)

# 324. Wiggle Sort II
# 376. Wiggle Subsequence