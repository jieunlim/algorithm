
# 242. Valid Anagram
# O(N)
# O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCnt = defaultdict(int)
        tCnt = defaultdict(int)

        for i in range(len(t)):
            tCnt[t[i]] += 1

        for i in range(len(s)):
            sCnt[s[i]] += 1

        if sCnt == tCnt:
            return True
        else:
            return False

    # O(N)
    # O(1)
    def isAnagram2(self, s: str, t: str) -> bool:
        sArr = [0 for _ in range(26)]
        tArr = [0 for _ in range(26)]

        for i in range(len(s)):
            sArr[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            tArr[ord(t[i]) - ord('a')] += 1

        if sArr == tArr:
            return True
        else:
            return False

s = 'ab'
t = 'b'
# s = 'a'
# t = 'b'
obj = Solution()
print(obj.isAnagram2(s, t))