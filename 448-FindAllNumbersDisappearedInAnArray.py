# 448. Find All Numbers Disappeared in an Array

class Solution:
    # Approach 1
    # Hash
    # O(n), O(n)
    def findDisappearedNumbers(self, nums):
        from collections import defaultdict
        dict = defaultdict(int)
        res = []
        for n in nums:
            dict[n] += 1

        for i in range(1, len(nums)+1):
            if i not in dict:
                res.append(i)
        return res

    # Approach 2
    # in-place modification solution
    # O(n), O(1)
    def findDisappearedNumbers2(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0: nums[idx] *= -1
            print(f"idx={idx}, nums={nums}")

        print(f"nums={nums}")
        res = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)

        return res

nums=[1,2,2,3,3,6]
obj = Solution()
print(obj.findDisappearedNumbers2(nums))