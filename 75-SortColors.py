# 75. Sort Colors
# time O(N), space O(1)
def sortColors(nums):
    p0 = curr = 0
    p2 = len(nums) - 1

    while curr <= p2:

        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1
        else:
            curr += 1

arr = [2,0,2,1,1,0]
arr = [2,0,1]
sortColors(arr)
print(arr)

