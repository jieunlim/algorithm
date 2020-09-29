#1.Two Sum - return indices of the two numbers
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
#hash table - O(n)
    def twoSum2(self, nums, target):

        if len(nums) <= 1:
            return

        d = {}
        for i, n in enumerate(nums):
            m = target - n

            if m in d:
                return [d[m], i]

            d[n] = i
#brute force - O(n2)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]



# Two Pointer
# Sort, remember indices
# https://leetcode.com/problems/two-sum/discuss/662/Python-dictionary-and-two-pointer-solutions.
    def twoSum3(self, nums, target):
        nums = enumerate(nums)
        nums= sorted(nums, key=lambda x:x[1])

        print(nums)

        i, j = 0, len(nums)-1
        while i < j:
            s = nums[i][1] + nums[j][1]
            if s == target:
                return [nums[i][0], nums[j][0]]
            elif s < target:
                i += 1
            else:
                j -= 1

        return -1


    def twoSum4(self, nums, target):
        if not nums: return -1

        nums2 = sorted(nums)

        i, j = 0, len(nums) - 1
        while i < j:

            a, b = nums2[i], nums2[j]
            if a + b == target:
                break
            elif a + b < target:
                i += 1
            else:
                j -= 1

        res = []
        for idx, n in enumerate(nums):
            if a == n:
                res.append(idx)
                break

        for idx, n in enumerate(nums):
            if a != b:
                if n == b:
                    res.append(idx)
                    break
            else:
                if res[0] != idx and n == b:
                    res.append(idx)
                    break

        return res

nums = [2, 7, 11, 15]
target = 18

obj = Solution()
print(obj.twoSum3(nums, target))