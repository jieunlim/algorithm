# 16. 3Sum Closest

#time limit exceeded
def threeSumClosest2(nums, target):

    nums.sort()
    res = {}

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                key_val = abs(target - (nums[i] + nums[j] + nums[k]))
                res.update({ key_val : nums[i] + nums[j] + nums[k]})

    # print(res)
    return res[min(res)]

# solution - O(n**2)
# https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return

        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                total  = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                if abs(target-total) < abs(target-res):
                    res = total

                if total < target:
                    l += 1
                else:
                    r -= 1

        return res

#
# def threeSumClosest(nums, target):
#
#     if len(nums) < 3:
#         return
#
#     nums.sort()
#     res = nums[0] + nums[1] + nums[2]
#     for i in range(len(nums)-2):
#         print(f"i = {i}")
#         j, k = i+1, len(nums)-1
#         while j < k:
#             sum = nums[i] + nums[j] + nums[k]
#             if sum == target:
#                 return sum
#
#             if abs(sum - target) < abs(res - target):
#                 res = sum
#
#             if sum < target:
#                 j += 1
#             else:
#                 k -= 1
#
#             print(f"res={res}, j={j}, k ={k}")
#     return res

nums = [-1, 2, 1, -4]
target = 1
obj = Solution()
print(obj.threeSumClosest(nums, target))