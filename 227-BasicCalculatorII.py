# 227. Basic Calculator II

# s[i], sign, num, stack

class Solution:
    def calculate(self, s):
        if not s: return "0"
        num, stack, sign = 0, [], "+"
        s += ' '
        print(f"s='{s}'")
        for i in range(len(s)):
            print(f"i={i}, s[i]='{s[i]}'")
            if s[i].isdigit():
                num = 10 * num + int(s[i])
                print(f"  1num={num}")
            elif (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                print(f"  2sign={sign}")
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    print(f" else  num={num}")
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
                print(f"stack={stack}, sign={sign}")
        return sum(stack)

    def calculate2(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            print(f"i={i}, s[i]={s[i]} ")
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                print(f"    num={num}")

            if s[i] in "+-*/" or i == len(s) - 1:
                print(f"    [if]")
                if sign == "+":
                    stack.append(num)
                    print(f"    +stack={stack}")
                elif sign == "-":
                    stack.append(-num)
                    print(f"    -stack={stack}")
                elif sign == "*":
                    stack.append(stack.pop()*num)
                    print(f"    *stack={stack}")
                else:
                    stack.append(int(stack.pop()/num))
                    print(f"    /stack={stack}")
                num = 0
                sign = s[i]
            print(f"    i={i}, num={num}, sign={sign}, stack={stack}")

        print(f"stack={stack}")
        return sum(stack)
s="3+2*2"
# s=" 3/2 "
# s="3/2"
# s="10-3/2"
# s="7-8-9*2"
# s="3+5/2"
# s=" 3+5 / 2 "
obj = Solution()
print(obj.calculate2(s))

# 224. Basic Calculator
# 772. Basic Calculator III