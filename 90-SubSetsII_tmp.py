class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def helper(idx, tmp):
            res.append(tmp) #1 assign tmp reference
            # res.append(tmp[:])  # 2 assign new array object
            print(f"idx={idx}, res={res}, tmp id={id(tmp)}, tmp={tmp}")
            for i in range(len(res)):
                print(f"res[{i}]={id(res[i])}")

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i - 1] == nums[i]:
                    continue
                tmp.append(nums[i])
                print(f"i={i}, idx={idx}, tmp={tmp}")
                helper(i + 1, tmp)
                tmp.pop()

        helper(0, [])
        return res

    def subsetsWithDup2(self, nums):
        def helper(start, path):
            print(f"start={start}, path={path}, {id(path)}, res={res}")
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: continue
                # path = path + [nums[i]]
                # helper(i+1, path)
                helper(i + 1, path + [nums[i]])

        res = []
        nums.sort()
        helper(0, [])
        return res


obj = Solution()
nums = [1, 2]
print(obj.subsetsWithDup(nums))
# print(obj.subsetsWithDup2(nums))