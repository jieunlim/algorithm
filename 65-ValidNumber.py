# 65. Valid Number

# https://leetcode.com/problems/valid-number/discuss/23738/Clear-Java-solution-with-ifs
# https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation

class Solution(object):
    def isNumber3(self, s: str) -> bool:
        s = s.strip()
        metE, metDot, metDigit = False, False, False

        for i, v in enumerate(s):
            if v in ['+', '-']:
                if i > 0 and s[i - 1] != 'e': return False
            elif v == 'e':
                if metE or not metDigit: return False
                metE, metDigit = True, False
            elif v == ".":
                if metDot or metE: return False
                metDot = True
            elif v.isdigit():
                metDigit = True
            else:
                return False

        return metDigit

    def isNumber(self, s):

        s = s.strip()
        print(f"s=[{s}]")
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

    def isNumber2(self, s):
        s = s.strip()
        if not s: return False
        metDigit, metE, metDot= False, False, False

        for i, ch in enumerate(s):
            if ch.isalpha():
                if ch != 'e': return False
                else:
                    if metE or not metDigit or i == 0 or i >= len(s)-1:
                        return False
                    metE = True
                    metDigit = False
            elif ch in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif ch == ".":
                if metE or metDot: return False
                metDot = True
            elif ch.isdigit():
                metDigit = True
            else:
                return False

        return metDigit

obj = Solution()


s = " " #false
s = ".1" #true
s= "3." #true
s=".e1" #false
s="4e+" #false
s="46.e3" #true
s=".e1" #false
# s="." #false
# s = "0" #=> true
# s = " 0.1 " #=> true
# s = "abc" #=> false
# s = "1 a" #=> false
# s = "2e10" #=> true
# s = " -90e3   " #=> true
# s = " 1e" #=> false
# s = "e3" #=> false
# s = " 6e-1" #=> true
# s = " 99e2.5 " #=> false
# s = "53.5e93" #=> true
# s = " --6 " #=> false
# s = "-+3" #=> false
# s = "95a54e53" #=> false

print(obj.isNumber(s))

# print(2e10)
# print(2e-4)
# print(2.3e5)