# 266. Palindrome Permutation
# O(N)
# O(1)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        sHash = defaultdict(int)
        for i in range(len(s)):
            sHash[s[i]] += 1

        cnt = 0
        for h in sHash:
            cnt += sHash[h]%2

        return False if cnt > 1 else True