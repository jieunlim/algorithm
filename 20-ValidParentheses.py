# 20. Valid Parentheses
# O(n), O(n)
# Stack, Dictionary
# for dealing with s='[', stack keeps '0'
# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    def isValid(self, s: str) -> bool:

        validDict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for p in s:
            if p in validDict:
                stack.append(p)
            else:
                if not stack or p != validDict[stack.pop()]:
                    return False
        return len(stack) == 0

    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(': ')', '[': ']', '{': '}'}
        print(f"stack={stack}, mapping={mapping}")
        for c in s:
            print(f"*c={c}")
            if c in mapping:
                stack.append(c)
                print(f"stack={stack}")
            else:
                p = stack.pop()
                print(f"mapping[p]={mapping[p]}, c={c}, {mapping[p] != c}")
                if mapping[p] != c: return False
        print(f"stackl={stack}")
        return stack == [0]

    #         dict = {0:None, '(':')', '{':'}', '[':']'}
    #         stack = [0]
    #         for c in s:
    #             if c in dict:
    #                 stack.append(c)
    #             else:
    #                 if c != dict[stack.pop()]: return False

    #         return stack == [0]

    def isValid2(self, s):
        dict = { '(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in dict:
                stack.append(ch)
            else:
                if stack == [] or dict[stack.pop()] != ch: return False
        return stack == []

s=']'
# s="(){[]}"
obj = Solution()
print(obj.isValid(s))

# 22. Generate Parentheses
# 32. Longest Valid Parentheses
# 301. Remove Invalid Parentheses
# 1003. Check If Word Is Valid After Substitutions