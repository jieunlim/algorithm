# 442. Find All Duplicates in an Array
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for x in nums:
        print(f"x={x}, nums={nums}, abs(x) - 1={abs(x) - 1}")
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
            print(res)
        else:
            nums[abs(x) - 1] *= -1
    return res

nums = [2,3,1,3]
print(findDuplicates(nums))

# 448. Find All Numbers Disappeared in an Array