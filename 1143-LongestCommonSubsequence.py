# 1143. Longest Common Subsequence

# time O(M*N) M*N subproblem, each subproblem has a cost of O(1)
# space O(M*N)

# https://youtu.be/ASoaQq66foQ

# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
# A common subsequence of two strings is a subsequence that is common to both strings.
#  
# If there is no common subsequence, return 0.

#https://comdoc.tistory.com/entry/34-가장-긴-공통-문자열-찾기-동적-프로그래밍
#recursion + memoization

def LCS1(w1, w2):

    def LCS_recursion(i, j):
        if i >= len(w1) or j >= len(w2):
            return 0

        # print(w1[i], w2[j], i, j)

        if (i,j) in memo:
            # print(f"return memoization i={i}, j={j}, {memo[(i,j)]}")
            return memo[(i,j)]

        if w1[i] == w2[j]:
            memo[(i,j)] = LCS_recursion(i+1, j+1) + 1
        else:
            memo[(i,j)] = max(LCS_recursion(i+1, j), LCS_recursion(i, j+1))

        return memo[(i,j)]

    memo={}
    return LCS_recursion(0,0)

w1="acddadef"
w2="acdgedef"
print(f"LCS1 - {LCS1(w1, w2)}\n")

#############################################
#???
A = "cddadef"
B = "acdgedef"
lcs = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
print(lcs)
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
print(lcs)
print(lcs[len(A)][len(B)])


# 583. Delete Operation for Two Strings
# 1092. Shortest Common Supersequence