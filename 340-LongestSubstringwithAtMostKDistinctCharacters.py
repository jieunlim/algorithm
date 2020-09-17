# 340. Longest Substring with At Most K Distinct Characters

# O(N) - N: the number of characters in the input string
# O(K) - we'll be storing a maximum of 'K+1' characters in the HashMap
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if len(s) < 1: return 0

        cnt, maxCnt, curK = 0, 0, 0
        chDict = defaultdict(int)
        start = 0

        for end, ch in enumerate(s):

            cnt += 1
            if ch not in chDict or chDict[ch] == 0:
                curK += 1
            chDict[ch] += 1

            while curK > k:
                chDict[s[start]] -= 1
                if chDict[s[start]] == 0:
                    curK -= 1
                    del chDict[s[start]]
                start += 1
                cnt -= 1

            maxCnt = max(maxCnt, cnt)
        return maxCnt

    def lengthOfLongestSubstringKDistinct2(self, s: str, k: int) -> int:
        start, curK, maxCnt = 0, 0, 0
        curDict = defaultdict(int)
        for end in range(len(s)):

            if curDict[s[end]] == 0:
                curK += 1
            curDict[s[end]] += 1

            while curK > k:
                curDict[s[start]] -= 1
                if curDict[s[start]] == 0:
                    curK -= 1
                start += 1

            print(start, end)
            cnt = end - start + 1
            if maxCnt < cnt: maxCnt = cnt

        return maxCnt


# end=2, start=0
# chDict = {'e':2, 'c':1}
# cnt=2
# maxCnt=2
# curK =2

s = 'aa'
k = 0

"abaccc"
2