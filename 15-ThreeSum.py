# 15. 3Sum
# SORT SORT SORT!!!!!

# Given an array nums of n integers
# Find all unique triplets in the array which gives the sum of zero
# O(N**2)

# Solution
# sort array, fix one element then move left and right pointers
def three_sum(nums, target):
    if len(nums) < 3:
        return
    elif len(nums) == 3:
        if sum(nums) == 0:
            return [sorted(nums)]

    res = []
    nums.sort()

    print(f"nums={nums}")
    for i in range(len(nums)):
        print(f"i={i}")
        if i > 0 and nums[i] == nums[i - 1]:
            print(f"continue i={i}")
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            print(f"l={l}, r={r}")
            total = nums[i] + nums[l] + nums[r]

            if total == target:
                print(f"[nums[i]={nums[i]}, nums[l]={nums[l]}, nums[r]]={nums[r]}")
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                    print(f"w   l={l}")
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                    print(f"w  r={r}")
                l += 1
                r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
            # print(f"i={i}, l={l}, r={r}, res={res}")
    return res

nums = [1, 0, -1, 0, -2, 2]
nums=[0,0,0,0]
# nums=[-3,-2,-1,0,0,1,2,3]
nums=[1,0,-1,0,-2,2]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6] #[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# nums = [-1, 0, 1, 2, -1, -4]
# nums=[0,0,0]
nums=[1,1,1,-1,0,2,2,0,1]
target=3
print(three_sum(nums, target))

