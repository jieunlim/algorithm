# 259. 3Sum Smaller
def threeSumClosest(nums, target):

    nums.sort()
    count = 0
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total < target:
                count += k-j
                j += 1
            else:
                k -= 1

    return count

nums=[-2,0,1,3]
target = 2
print(threeSumClosest(nums, target))
