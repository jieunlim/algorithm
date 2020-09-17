# 161. One Edit Distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        i, j, lenS, lenT = 0, 0, len(s), len(t)
        flag = False
        if lenS + 1 == lenT:  # insert
            while i < lenS and j < lenT:
                if s[i] != t[j]:
                    if flag: return False
                    j += 1
                    flag = True
                else:
                    i += 1
                    j += 1

            return True  # a, aa
        elif len(s) == len(t) + 1:  # delete
            while i < lenS and j < lenT:
                if s[i] != t[j]:
                    if flag: return False
                    i += 1
                    flag = True
                else:
                    i += 1
                    j += 1

            return True
        elif len(s) == len(t):  # replace
            while i < lenS and j < lenT:
                if s[i] != t[j]:
                    if flag: return False
                    i += 1
                    j += 1
                    flag = True
                else:
                    i += 1
                    j += 1
            if flag: return True
        return False
