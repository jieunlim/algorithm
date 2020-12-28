# 516. Longest Palindromic Subsequence
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
# "bbbab" --> 4
#MIT Lecture10 DP


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def helper(i, j):
            if i > j: return 0
            if i == j: return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = 2 + helper(i + 1, j - 1)
            else:
                memo[(i, j)] = max(helper(i + 1, j), helper(i, j - 1))

            return memo[(i, j)]

        if not s: return -1
        memo = {}
        return helper(0, len(s) - 1)



def lps1(s, i, j):

    if i > j:
        print("return 0", i, j)
        return 0

    print(i, j)
    if i == j:
        return 1

    if s[i] == s[j]:
        rtn = lps1(s, i+1, j-1) + 2
    else:
        rtn = max(lps1(s, i+1, j), lps1(s, i, j-1))

    return rtn


def lps(str):

    def lpsRe(i, j):
        if i > j:
            return 0

        if str[i] == str[j]:
            if i == j:
                return 1
            else:
                return lpsRe(i+1, j-1) + 2
        else:
            return max(lpsRe(i+1, j), lpsRe(i, j-1))

    if str == "":
        return -1
    return lpsRe(0, len(str)-1)


# memoization
def lps2(str):

    def L(i, j):

        print(f"i={i}, j={j}")
        if i == j:
            print("return 1 i==j")
            return 1

        if (i, j) in memo:
            print(f"return memoization {memo[(i,j)]}")
            return memo[(i,j)]

        print(f"{str[i]}, {str[j]}")
        if str[i] == str[j]:
            if i+1 == j:
                print("return 2  --> i+1 == j")
                memo[(i,j)] = 2
            else:
                memo[(i,j)]= 2+L(i+1, j-1)
        else:
            memo[(i,j)]= max(L(i+1, j), L(i, j-1))

        return memo[(i,j)]

    memo = {}
    return(L(0, len(str)-1))



# str="turboventilator"
# str="radar"
str="redder"
str="babad"
# str="babe"
print(lps2(str))
print(lps2(str))


# from functools import lru_cache
# @lru_cache(None)




def longestPalindromeSubseq(s):
    if s == s[::-1]:
        return len(s)

    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    print(dp)

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            print(f"i={i}, j={j}, dp={dp}")
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            print(    dp)

    return dp[0][n - 1]




def longestPalindromeSubseq111(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s)
    dp = [[0] * l for _ in range(l)]

    for i in range(l):
        dp[i][i] = 1

    for i in range(l - 1, -1, -1):
        for j in range(i + 1, l):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][l - 1]

    # for i in range(l - 1, -1, -1):
    #     for j in range(i + 1, l):
    #         if s[i] == s[j]:
    #             dp[i][j] = dp[i + 1][j - 1] + 2
    #         else:
    #             dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    # return dp[0][l - 1]

#     b b b a b
#     0 1 2 3 4
# b 0 1 2 3 3 4
# b 1   1 2 2 3
# b 2     1 1 3
# a 3       1 1
# b 4         1

# 0,1 -> 1,2 -> 2,3 -> 3,4
# 0,2 -> 1,3 -> 2,4

# a b c b a

#       c b b d
#       0 1 2 3
# c 0   1 1 2 2
# b 1     1 2 2
# b 2       1 1
# d 3         1