
# 583. Delete Operation for Two Strings
# time O(m*n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def helper(i, j):

            if i >= len(word1): return len(word2) - j
            if j >= len(word2): return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i + 1, j + 1)
            else:
                memo[(i, j)] = min(helper(i + 1, j), helper(i, j + 1)) + 1

            return memo[(i, j)]

        memo = {}
        return helper(0, 0)

# 1143. Longest Common Subsequence

def deleteTwo(t1, t2):

    def DT(t1, t2):
        print(f"t1={t1}, t2={t2}, memo={memo}")
        if not t1:
            return len(t2)
        elif not t2:
            return len(t1)

        if (t1, t2) in memo:
            return memo[(t1, t2)]

        if t1[0] == t2[0]:
            memo[(t1, t2)] = DT(t1[1:], t2[1:])
        else:
            memo[(t1, t2)] = min(DT(t1[1:], t2), DT(t1, t2[1:])) + 1
        return memo[(t1, t2)]

    memo = {}
    return DT(t1, t2)

t1 = "sea"
t2 = "eat"
t1 = "dinitrophenylhydrazine"
t2 = "acetylphenylhydrazine"
print(deleteTwo(t1, t2))

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103267/Python-Straightforward-with-Explanation
