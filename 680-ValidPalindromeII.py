
# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def getResult(i, j):

            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        i, j = 0, len(s) - 1
        k = 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return getResult(i + 1, j) or getResult(i, j - 1)
        return True


# aiacaiaa
# ababca

# O(N)
#    O(1)

def validPalindrome2(s: str) -> bool:
    def helper(x, y):
        while x < y:
            if s[x] != s[y]:
                return False
            x += 1
            y -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return helper(i + 1, j) or helper(i, j - 1)
    return True

# https://leetcode.com/problems/valid-palindrome-ii/discuss/209252/Java-Python-Two-Pointers-with-Thinking-Process
def validPalindrome( s):

    def validPalindromeUtil(i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return validPalindromeUtil(i + 1, j) or validPalindromeUtil( i, j - 1)
    return True

s="aba"
print(validPalindrome(s))

# 678. Valid Parenthesis String
# 22. Generate Parentheses
# 527. Word Abbreviation