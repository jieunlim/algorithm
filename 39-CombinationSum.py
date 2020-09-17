# 39. Combination Sum
# time complexity
# O(N^t) N: # of candidates, t: target
# N choice every time, and we can choose at most target times(height of tree)
# https://youtu.be/MTI2wc8s0BY
# space : O(target) : recursive calls


# backtracking
# https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
# https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A

# I think the time complexity of this is O(#candidates^target)
# because the height of the tree would be target
# and degree of each node would be number of candidates.
# A more accurately expression may be O(#candidates^(target/min of candidates))

# Space complexity is O(target)
def combinationSum(candidates, target):

    def helper(start, total, path):
        if total == target:
            res.append(path)
            return

        for i in range(start, len(candidates)):
            t = total+candidates[i]
            if t > target: break
            helper(i, t, path +[candidates[i]])

    if not candidates: return []
    res = []
    candidates.sort()
    helper(0, 0, [])
    return res

candidates = [1, 2]
target = 3
print(combinationSum(candidates, target))

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target: break
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

class Solution2:
    def combinationSum(self, nums, target):
        res = []
        nums.sort()
        def dfs(left, path, idx):
            if not left: res.append(path[:])
            else:
                for i, val in enumerate(nums[idx:]):
                    if val > left: break
                    dfs(left - val, path + [val], idx + i)
        dfs(target, [], 0)
        return res

class Solution3:
    def combinationSum(self, candidates, target):

        def dfs(target, path, idx):
            print(f"target={target}, path={path}, idx={idx}")
            if target == 0:
                res.append(path)
                print(f"   return  target={target}, res={res}")
                return

            for i, val in enumerate(candidates[idx:]):
                print(f"  i={i}, val={val}")
                if val > target:
                    print(f"  break")
                    break
                print(f"  call dfs ")
                dfs(target - val, path + [val], idx + i)
                print(f"  after dfs target={target}, idx={idx}")

        res = []
        candidates.sort()

        dfs(target, [], 0)
        return res

candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
candidates = [2,3]
target = 7
obj = Solution()
print(obj.combinationSum(candidates, target))

# 322. Coin Change


'''
# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [i  for i in range(1,10)]
        def backtrack(nums,index,n,k,path):
            if n < 0:
                return
            if k == 0 and n == 0:
                result.append(path)
                return
            for i in range(index,len(nums)):
                if nums[i] > n:
                    continue
                backtrack(nums,i+1,n-nums[i],k-1,path+[nums[i]])
        backtrack(nums,0,n,k,[])
        return result
'''