# 227. Basic Calculator II

# s[i], sign, num, stack

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = '+'
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                
            if s[i] in '+-*/' or i == len(s)-1: # put last number in the stack
                if sign in '+-':
                    stack.append(int(sign+str(num)))

                elif sign == '*':
                    prev = stack.pop()
                    stack.append(num * prev)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev/num))   
                sign = s[i]
                num = 0
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
