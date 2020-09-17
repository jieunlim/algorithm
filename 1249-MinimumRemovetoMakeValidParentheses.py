# 1249. Minimum Remove to Make Valid Parentheses

# O(n)
# O(n)
class Solution:
    def minRemoveToMakeValid(self, s):
        # stack = [(,(]
        # ) -> if stack[-1], (
        # stack

        # res = 'a'
        # ) -> remove
        # res = 'ab'
        # (
        # stack=[]
        # res = 'ab(c)'

        # ) - remove
        # ) - remove
        # [0,1] res=((

        if not s: return ''

        resStr = ''
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                resStr += ch
                stack.append(len(resStr) - 1)

            elif ch == ')' and stack:
                resStr += ch
                stack.pop()

            elif ch.isalpha():
                resStr += ch

        resStr2 = ''
        print(resStr, stack)
        for i in range(len(resStr)):
            if i not in stack:
                resStr2 += resStr[i]

        return resStr2

s = "lee(t(c)o)de)"
s = "a)b(c)d"
s = "))(("
s = "(a(b(c)d)"
s = ')a(b'
obj = Solution()
print(obj.minRemoveToMakeValid(s))