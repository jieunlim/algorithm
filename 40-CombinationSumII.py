# 40. Combination Sum II

# DFS, backtracking
# O(2^^n)

# 39. Combination Sum
# Time complexity: N ^ (t/m), N: # of candidates, t: target, m: minimum value of candidates
#
# 40. Combination Sum II
# Time complexity: 2^N, N: # of candidates
#
# 입력값 candidates = [2,3,5], target = 8 인 경우,
# 39의 경우, 같은 수가 반복해서 들어갈 수 있고
# 40의 경우 같은 수는 한번만 사용 (40문제에서, 중복된 결과가 없도록 하는 처리는 논외로 두고요)
#
# 39의 경우, N-ary tree가 만들어집니다.
# 맨 위에 2, 3, 5 가 있고, 2가 반복 사용되면서 target 크기 만큼 높이가 생기게되죠. 여기서 2는 array에서 가장 작은 값입니다. 그래서 N개가 target/minumim value만큼의 tree height가 되어,
# Time complexity는 N ^ (t/m) 입니다.
#
# 40 의 경우, 같은 값이 반복되지 않기 때문에 tree는 훨씬 간단하게 생기며, 이 갯수는 그냥 2^N입니다.
# 매번 조건이 내가 포함되는 경우와 아닌 두가지 경우.

class Solution:
    def combinationsSum2(self, candidates, target):

        self.gCnt = 0
        def helper(start, target, path):
            print(f"* start={start}, path={path}, target={target}")
            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                self.gCnt += 1
                print(self.gCnt)
                print(f"  i={i}, start={start}")
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                t = target - candidates[i]
                if t < 0: break
                helper(i + 1, t, path + [candidates[i]])
                print(f"res={res}, i={i}, start={start}")

        res = []
        candidates.sort()
        helper(0, target, [])
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
# candidates=[2,5,2,1,2]
# target=5
candidates = [0,1] #4
target = 2
candidates = [2,3,5] #8
target = 8
# candidates = [0,1,2,3] #16
# target = 7
# candidates = [0,1,2,3,4] #32
# target = 10
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