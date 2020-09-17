# 403. Frog Jump
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        def jump(idx, jumpCnt):
            # print(f"*idx={idx}, jumpCnt={jumpCnt}")
            if idx == stones[-1]:
                return True

            if idx >= stones[-1]:
                return False

            if (idx, jumpCnt) in memo:
                return memo[(idx, jumpCnt)]

            for j in range(jumpCnt - 1, jumpCnt + 2):
                if j > 0 and idx + j in stones:
                    # print(f" idx={idx}, j={j}")
                    if jump(idx + j, j):
                        memo[(idx, jumpCnt)] = True
                        return True

            memo[(idx, jumpCnt)] = False
            return False

        memo = {}
        return jump(0, 0)

stones=[0,1,3,5,6,8,12,17] #T
stones = [0,1,2,3,4,8,9,11] #F
stones=[0,2]
obj = Solution()
print(obj.canCross(stones))


class Solution:
    def canCross(self, stones):

        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        # dfs
        candidate = [speed - 1, speed, speed + 1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False




from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        from collections import defaultdict

        crossDict = defaultdict(list)
        for stone in stones:
            crossDict[stone].append(-1)
        crossDict[0].append(0)
        print(f"crossDict={crossDict}")

        for st in stones:
            for c in crossDict[st]:

                for j in range(c - 1, c + 2):
                    if j <= 0: continue
                    if st + j in crossDict:
                        print(f"st={st}, c={c}, j={j}, st + j={st + j}")
                        if j not in crossDict[st + j]:
                            crossDict[st + j].append(j)
                            print(f"  crossDict[st+j]={crossDict[st+j]}")
                        if st + j == stones[-1]: return True

        # print(crossDict)
        return False

stones = [0,1,3,5,6,8,12,17]
obj = Solution()
# print(obj.canCross(stones))