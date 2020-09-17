# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# "babad" -> "bab", "cbbd"->"bb"

# string : consecutive
# sequence : particular order

# ?  O(n^2), O(1)

def longestPalindrome(s):

    def helper(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            print(f"        l={l}, r={r}")
        print(f"   l={l}, r={r}, s[{l + 1}:{r}]={s[l + 1:r]}")
        return s[l + 1:r]

    res = ""
    for i in range(len(s)):
        print(f"*i={i}")
        res = max(helper(i, i), helper(i, i + 1), res, key=len)
        print(f"    res={res}")
    return res



# str="turboventilator"
# str="character"
str="radar"

# str="babad"
# str="babed"
# str="redder"
# print(lps(str))
print(longestPalindrome(str))

from collections import defaultdict
def palindromePermutation(s):
    sHash = defaultdict
    for i in range(len(s)):
        sHash[s[i]] += 1

    for i in sHash:
        cnt += sHash[s[i]]%2

    return False if cnt > 1 else True