# 763. Partition Labels
class Solution:
    def partitionLabels(self, S: str):

        if S == '': return 0
        idxDict = defaultdict(int)
        for i, ch in enumerate(S):
            idxDict[ch] = i

        maxIdx = idxDict[S[0]]
        res, cnt = [], 0
        for i, ch in enumerate(S):

            cnt += 1

            if idxDict[ch] > maxIdx:
                maxIdx = idxDict[ch]

            if maxIdx == i:
                res.append(cnt)
                cnt = 0

        return res

    def partitionLabels2(self, S: str):

        if S == '': return []

        maxIdxDict = defaultdict(int)
        for i, ch in enumerate(S):
            maxIdxDict[ch] = i

        res, j = [], 0
        maxIdx = maxIdxDict[S[0]]
        for i, ch in enumerate(S):
            maxIdx = max(maxIdx, maxIdxDict[ch])
            if maxIdx == i:
                res.append(i - j + 1)
                j = i + 1
        return res
#  i=3, ch=d, cnt=1
#  maxIdx =2
# aba/d

#     abeade  -> abeade
#     a:3, b:1, e:5, d:4
#       maxV=3
