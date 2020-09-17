# 46. Permutations
# n numbers of set
# time O(n!), space O(n!)


# ?
# each node operation is O(n), the number of nodes is n! --> O(n*n!)
# space O(n*n!) for output
# time complexity 11:40  https://www.youtube.com/watch?v=KukNnoN-SoY

class Solution:
    def permute(self, nums):

        def backtracking(subset):
            if len(subset) == numsLen:
                res.append(subset)
                return

            for i in range(numsLen):
                if i not in visited:
                    visited.add(i)
                    backtracking(subset+[nums[i]])
                    visited.remove(i)

        numsLen = len(nums)
        res = []
        visited = set()
        backtracking([])
        return res

    # https: // leetcode.com / problems / permutations / discuss / 360280 / Python3 - backtracking
    def permute2(self, nums):

        def backtracking(subset):

            print(f"backtracking res={res}, visited={visited},subset={subset}, nums={nums} ")

            if len(subset) == len(nums):
                res.append(subset)
                print(f"return, res={res}")
                return

            for i in range(len(nums)):
                print(f"i={i}")
                if i not in visited:
                    visited.add(i)
                    print(f"visited={visited}")
                    backtracking(subset + [nums[i]])
                    print(f"remove i={i}")
                    visited.remove(i)

        visited = set()
        res = []
        backtracking([])
        return res

nums = [1, 2, 3]
obj = Solution()
print(obj.permute(nums))

'''
def permute(self, nums):
    def backtrack(first=0):
        # if all integers are used up
        print(f"first={first}")

        if first == n:
            output.append(nums[:])
            print(f" output={output}")

        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            print(f"-i={i}, first={first}, nums[{first}]={nums[first]}, nums[{i}]={nums[i]}")

            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
            # print(f"----i={i}, first={first}, nums[{first}]={nums[first]}, nums[{i}]={nums[i]}, output={output}")

    n = len(nums)
    output = []
    backtrack()
    return output
'''
# def bt(first):
#
#     if first ==  n:
#         output.append(nums)
#
#     for i in range(first, n):
#         nums[first], nums[i] = nums[i], nums[first]
#         bt(first+1)
#         nums[first], nums[i] = nums[i], nums[first]
#
# nums = [1, 2, 3]
# n=len(nums)
# output = []
# bt(0)
# print(output)


'''  
# DFS
    def permute_dfs(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        print(f"*{nums}")
        if not nums:
            print(f"res.append({path})")
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            print(f"i={i}, nums[:i] ={nums[:i]}, nums[i + 1:]={nums[i + 1:]}, path={path}, [nums[i]]={[nums[i]]}, res={res}")
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# print(obj.permute_dfs(nums))

# [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 3, 2], [1, 4, 2, 3],
#  [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 3, 1], [2, 4, 1, 3],
#  [3, 2, 1, 4], [3, 2, 4, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1],
#  [4, 2, 3, 1], [4, 2, 1, 3], [4, 3, 2, 1], [4, 3, 1, 2], [4, 1, 3, 2], [4, 1, 2, 3]]

'''