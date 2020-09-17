# 767. Reorganize String

# count the most frequent letter
# a:2, b:1

# https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        res, c = [], Counter(S)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        print(f"res={res}, pq={pq}")
        pCnt, pCh = 0, ''
        while pq:
            cnt, ch = heapq.heappop(pq)
            res += [ch]
            print(f" cnt={cnt}, ch={ch}, res={res}, pCnt={pCnt}")
            if pCnt < 0:
                heapq.heappush(pq, (pCnt, pCh))
                print(f"  pq={pq}")
            cnt += 1
            pCnt, pCh = cnt, ch
            print(f"cnt={cnt}, pCnt={pCnt}, pCh={pCh}")
        print(f"res={res}")
        res = ''.join(res)
        print(f"res={res}")
        if len(res) != len(S): return ""
        print(f"res={res}")
        return res

    def reorganizeString2(self, S):
        import collections
        count = collections.Counter(S).most_common()
        N = len(S)
        if count[0][1] > (N + 1) // 2: return ''
        ans = [''] * N
        i = 0
        for letter, cnt in count:
            for c in range(cnt):
                ans[i] = letter
                i += 2
                if i >= N:
                    i = 1
        return ''.join(ans)
    #     hash = [0 for _ in range(26)]
    #     for i in range(len(S)):
    #         hash[ord(S[i]) - ord('a')] += 1
    #     print(f"hash={hash}")
    #     max, letter = 0, 0
    #     for i in range(len(hash)):
    #         if hash[i] > 0:
    #             max = hash[i]
    #             letter = i
    #     if max > ((len(S)+1)//2):
    #         return ''
    #
    #     idx, res = 0, ''
    #     while hash[letter] > 0:
    #         res[idx] = str(letter+ord('a'))
    #         idx += 2
    #         hash[letter] -= 1
    #
    #     for i in range(len(hash)):
    #         while hash[i] > 0:
    #             if idx >= len(res):
    #                 idx = 1
    #             res[idx] = str(i +'a')
    #             idx += 2
    #             hash[i] -= 1
    #     return res


obj = Solution()
S = "aab"
# S='aaaabb'
print("result:", obj.reorganizeString2(S))


# 621. Task Scheduler