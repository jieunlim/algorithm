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


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        def helper(s, t, option):
            flag, i, j = False, 0, 0
            while i < len(s) and j < len(t):
                print(f"option={option}, flag={flag}")
                if s[i] != t[j]:
                    if flag: return False
                    if option == 1:
                        j += 1
                    elif option == 2:
                        i += 1
                    else:
                        i += 1
                        j += 1
                    flag = True
                    print(f"flag={flag}")
                else:
                    i += 1
                    j += 1

            if option in (1, 2):
                flag = True

            if flag:
                return True
            else:
                return False

        lenS = len(s)
        lenT = len(t)
        #         insert
        if lenS + 1 == lenT:
            return helper(s, t, 1)
        #         delete
        elif lenS == lenT + 1:
            return helper(s, t, 2)
        #         replace
        elif lenS == lenT:
            return helper(s, t, 3)