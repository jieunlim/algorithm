# 516. Longest Palindromic Subsequence
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
# "bbbab" --> 4
#MIT Lecture10 DP

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
