# 90. Subsets II
# time O(2^N)
# space O(2^N)
def subsetsWithDup(nums):

    def helper(start, path):
        print(f"start={start}, path={path}, {id(path)}, res={res}")
        res.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            # path = path + [nums[i]]
            # helper(i+1, path)
            helper(i+1, path + [nums[i]])
    res = []
    nums.sort()
    helper(0, [])
    return res

def subsetsWithDup2(nums):
    def helper(start, path):
        print(f"start={start}, path={path}, {id(path)} res={res}")
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            path.append(nums[i])
            helper(i+1, path)
            path.pop()
    res = []
    nums.sort()
    helper(0, [])
    return res

nums=[1,2,2]
print(subsetsWithDup(nums))
print(subsetsWithDup2(nums))