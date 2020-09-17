# 22. Generate Parentheses

# time complexity:
# about n, the options could be binary tree, the tree could be 2n level.
# The number of node would be 2^2n
# so, time complexity is O(2^2n)
# space complexity is O(n) for storing sequence(path)

class Solution:
    def generateParenthesis(self, n):
        def gen(left, right, genParen):
            if right < left:
                return

            if not left and not right:
                res.append(genParen)
                return

            if left:
                gen(left-1, right, genParen + '(')
            if right:
                gen(left, right-1, genParen + ')')

        res = []
        gen(n, n, '')
        return res


    def generateParenthesis2(self, n):
        def helper(s1, s2, path):
            print(f"s1={s1}, s2={s2}, path{path}")
            if s1> s2 :
                return

            if len(path) == 2*n:
                res.append(path)

            if s1 > 0: helper(s1-1, s2, path + '(')
            if s2 > 0:helper(s1,s2-1, path + ')')

    res = []
    helper(n, n, '')
    return res
n=2
obj = Solution()
print(obj.generateParenthesis(n))


# backtracking
# https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
# If you have two stacks, one for n "(", the other for n ")",
# you generate a binary tree from these two stacks of left/right parentheses to form an output string.
# This means that whenever you traverse deeper, you pop one parentheses from one of stacks.
# When two stacks are empty, you form an output string.
# How to form a legal string? Here is the simple observation:
# For the output string to be right, stack of ")" most be larger than stack of "(". If not, it creates string like "())"
# Since elements in each of stack are the same, we can simply express them with a number.
# For example, left = 3 is like a stacks ["(", "(", "("]

# time O(2^2n), binary tree, 2n level
# O(2 ^ 2n) since we need n pairs, which makes 2n parentheses to add.
# And for the power 2 does make difference in terms of big O, so we shouldn't ignore it.
# space O(n)

# Catalan number - 1,1,2,5,14,42 (n=0,1,2,3,4,5..)
# https://suhak.tistory.com/77
# The way I like to think about the runtime of backtracking algorithms is O(b^d),
# where b is the branching factor and d is the maximum depth of recursion.
# Backtracking is characterized by a number of decisions b that can be made at each level of recursion.
# If you visualize the recursion tree, this is the number of children each internal node has.
# You can also think of b as standing for "base", which can help you remember that b is the base of the exponential.
# If we can make b decisions at each level of recursion,
# and we expand the recursion tree to d levels
# (ie: each path has a length of d), then we get b^d nodes.
# Since backtracking is exhaustive and must visit each one of these nodes, the runtime is O(b^d).

'''
def generageP(n):

    def helper(left, right, path = ''):

        if left > right:
            return
        elif left <0 or right <0:
            return

        if len(path) == 2*n:
            res.append(path)

        helper(left-1, right, path + '(')
        helper(left, right-1, path + ')')

    res = []
    helper(n, n)
    return res
'''