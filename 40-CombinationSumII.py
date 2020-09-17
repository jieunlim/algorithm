# 40. Combination Sum II

# DFS, backtracking
# O(n^^2)
class Solution:
    def combinationsSum2(self, candidates, target):
        def helper(start, target, path):

            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                t = target - candidates[i]
                if t < 0: break
                helper(i + 1, t, path + [candidates[i]])

        res = []
        candidates.sort()
        helper(0, target, [])
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
# candidates=[2,5,2,1,2]
# target=5
obj = Solution()
print(obj.combinationsSum2(candidates, target))


# def CS(t, path, idx):
#     print(f"t={t}, path={path}, idx={idx}")
#     if t == 0:
#         print(f"***path={path}")
#         res.append(path)
#         return
#
#     if idx >= lenC:
#         return
#
#     for i in range(idx, lenC):
#         candi = candidates[i]
#         print(f"candi={candi}")
#         if (i > idx and candi == candidates[i - 1]) or candi > t: continue
#         CS(t - candi, path + [candi], i + 1)
#
#
# res = []
# lenC = len(candidates)
# candidates.sort()
# print(candidates)
# CS(target, [], 0)
# return res