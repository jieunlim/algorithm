# 47. Permutations II
# O(N!)
# O(N!)

import collections
class Solution:
    def permuteUnique2(self, nums):
        def backtrack(path):

            if len(path) == len(nums):
                res.add(tuple(path))
                return

            for k in range(len(nums)):
                if k not in visited:
                    visited.add(k)
                    backtrack(path + [nums[k]])
                    visited.remove(k)

        if not nums: return []
        res = set()
        visited = set()
        backtrack([])

    def permuteUnique(self, nums):
        def helper(path):
            if len(path) == len(nums):
                res.append(path)
                print(f"res={res}, counter={counter}")
                return

            for i in range(len(nums)):
                print(f"i={i}, counter={counter}, path={path}")
                if counter[nums[i]] > 0 and (i == 0 or (i > 0 and nums[i] != nums[i - 1])):
                    counter[nums[i]] -= 1
                    helper(path + [nums[i]])
                    counter[nums[i]] += 1

        if not nums: return []
        res = []
        counter = collections.Counter(nums)
        nums.sort() #should!
        helper([])
        return res

    return list(res)
nums = [1, 2, 2]
obj = Solution()
print(obj.permuteUnique(nums))

'''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def helper(path):
            if len(path) == len(nums):
                res.append(path)
                return

            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    helper(path + [key])
                    counter[key] += 1

        counter = collections.Counter(nums)
        res = []
        helper([])
        return res
'''