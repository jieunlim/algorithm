
# 224. Basic Calculator

# Implement a basic calculator
# contain open ( and closing parentheses )
# , the plus + or minus sign -, non-negative integers and empty spaces .

# stack
# time complexity O(N), N is the length of the string
# space O(N)

# https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
class Solution:
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            print(f"ss={ss}")
            if ss.isdigit():
                num = 10 * num + int(ss)
                print(f"    1num={num}, sign={sign}")
            elif ss in ["-", "+"]:
                print(f"    2res={res}, sign={sign}, num={num}")
                res += sign * num
                num = 0
                sign = [-1, 1][ss == "+"]
                print(f"    2res={res}, sign={sign}, num={num}")
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
                print(f"    3stack={stack}")
            elif ss == ")":
                res += sign * num
                print(f"    4res={res}, stack={stack}")
                res *= stack.pop()
                print(f"    res={res}, stack={stack}")
                res += stack.pop()
                print(f"    res={res}, stack={stack}")
                num = 0
                print(f"    4res={res}")
        print(f"res {res}  + num {num} * sign {sign}")
        return res + num * sign

    # https://leetcode.com/problems/basic-calculator/discuss/62418/Python-with-stack
    # This solution uses stack to store previous result and sign when encounter a "("
    # For this problem storing sign is enough, and will be faster.
    def calculate2(self, s):
        res, num, sign, stack = 0, 0, 1, [1]
        print(f"s={s}")
        for i in s+"+":
            print(f"i={i}")
            if i.isdigit():
                num = 10*num + int(i)
                print(f"    isdigit, num={num}, sign={sign}")
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i=="+" else -1
                num = 0
                print(f"    +-, res={res}, sign={sign}")
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
                print(f"    (, stack={stack}, sign={sign}")
            elif i == ")":
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
                print(f"    ), res={res}, num={num}, stack={stack}")
        return res

s = "1 + 1"
# s=" 2-1 + 2 "
# s="(1+(4+5+2)-3)+(6+8)"
s="7-(8+9)"
obj = Solution()
print(obj.calculate(s))



# 227. Basic Calculator II
# 772. Basic Calculator III