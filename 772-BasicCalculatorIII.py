# 772. Basic Calculator III

# https://leetcode.com/problems/basic-calculator-iii/discuss/127881/Python-O(n)-Solution-using-recursion
class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(s.split())
        L = len(s)

        def getOpd(i):
            if s[i] == '(':
                return evalExpr(i + 1, L)
            else:
                i, isNeg = (i + 1, True) if s[i] == '-' else (i, False)
                j = i
                while j < L and s[j].isdecimal(): j += 1
                return -int(s[i:j]) if isNeg else int(s[i:j]), j

        def evalExpr(beg, end):
            res, i = getOpd(beg)
            stack = [res]

            while i < end:
                operator = s[i]
                i += 1
                if operator == ')': break

                opd, i = getOpd(i)

                if operator == '+':
                    stack.append(opd)
                elif operator == '-':
                    stack.append(-opd)
                elif operator == '*':
                    stack.append(opd * stack.pop())
                elif operator == '/':
                    stack.append(int(stack.pop() / opd))

            return sum(stack), i

        return evalExpr(0, L)[0]

    def calculate2(self, s):
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            print(f"[helper] num={num}, sign={sign}")

            while i < len(s):
                c = s[i]
                print(f"[while] i={i}, c={c}")
                if c == " ":
                    i += 1
                    print(f"    continue i = {i}")
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                    print(f"    digit - num={num}, i={i}")
                elif c == '(':
                    print(f"    ( - call helper")
                    num, i = helper([], i+1)
                    print(f"    ( - after call helper num={num}, i={i}")
                else:
                    print(f"    else")
                    if sign == '+':
                        stack.append(num)
                        print(f"    +stack={stack}")
                    if sign == '-':
                        stack.append(-num)
                        print(f"    -stack={stack}")
                    if sign == '*':
                        print(f"    *stack={stack}, num={num}")
                        stack.append(stack.pop() * num)
                        print(f"    *stack={stack}")
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                        print(f"    /stack={stack}")
                    num = 0
                    i += 1
                    print(f"num={num}, i={i}")
                    if c == ')':
                        print(f"    ) return sum(stack), i {sum(stack)}, {i}")
                        return sum(stack), i
                    sign = c
                    print(f"sign = {sign}")
            print(f"return sum(stack)={sum(stack)}")
            return sum(stack)
        return helper([], 0)

s="12-(5+2)*4"
# s="2+3 "
obj = Solution()
print(obj.calculate2(s))


'''
    # postfix
    
	(2+6*3+5-(3*14/7+2)*5)+3		3가지 경우의수 
	Stack(Operator)	String	
(	(	""	
2		2	
"+"	(+	2	
6	(+	26	
"*"	(+*	26	
3	(+*	263	
"+"	(+	263*+	
5	(+	263*+5	
"-"	(-	263*+5+	
(	(-(	263*+5+	
3	(-(	263*+5+3	
"*"	(-(*	263*+5+3	
14	(-(*	2,6,3*+5+3,14	
/	(-(/	2,6,3*+5+3,14*	
7	(-(/	2,6,3*+5+3,14*7	
"+"	(-(+	2,6,3*+5+3,14*7/	
2	(-(+	2,6,3*+5+3,14*7/2	
)	(-	2,6,3*+5+3,14*7/2+	닫는 포인트
*	(-*	2,6,3*+5+3,14*7/2+	
5	(-*	2,6,3*+5+3,14*7/2+5	
)		2,6,3*+5+3,14*7/2+5*-	
"3"		2,6,3*+5+3,14*7/2+5*-3+	
"+"		2,6,3*+5+3,14*7/2+5*-3+	
'''

'''

class Solution0224 {
    int index = 0;
    String str;

    int getNum() {
        int ret = 0;
        while(index < str.length()) {
            char c = str.charAt(index);
            if (c >= '0' && c <= '9') {
                ret = (ret * 10 + (c - '0'));
            } else {
                return ret;
            }
            index++;
        }
        return ret;
    }
    int cal() {
        int ret = 0;
        int mul = 1;

        while (index < str.length()) {
            switch(str.charAt(index)) {
                case ' ':
                    index++;
                    break;
                case '+':
                    mul = 1;
                    index++;
                    break;
                case '-':
                    mul = -1;
                    index++;
                    break;
                case '(':
                    index++;
                    ret += (mul*cal());
                    break;
                case ')':
                    index++;
                    return ret;
                default:
                    ret += (mul*getNum());
            }
        }

        return ret;
    }

    public int calculate(String s) {
        index = 0;
        str = s;
        return cal();
    }
}



772. Basic Calculator III
class Solution0772 {
    int index = 0;
    String str;

    class Node {
        int value;
        int operator;
        Node(int v, int o) {
            value = v;
            operator = o;
        }
    }

    int getNum() {
        int ret = 0;
        while(index < str.length()) {
            char c = str.charAt(index);
            if (c >= '0' && c <= '9') {
                ret = (ret * 10 + (c - '0'));
            } else {
                return ret;
            }
            index++;
        }
        return ret;
    }

    int cal() {
        int ret = 0;
        int mul = 1;
        ArrayList<Node> queue = new ArrayList<>();

        while (index < str.length()) {
            char c = str.charAt(index);
            if (c == ' ') index++;
            else if (c == '+') {
                queue.add(new Node(ret, 1));
                index++;
            } else if (c == '-') {
                queue.add(new Node(ret, -1));
                index++;
            } else if (c == '(') {
                index++;
                ret = cal();
                if (queue.size() > 0 && queue.get(queue.size() - 1).operator >=3) {
                    Node n = queue.get(queue.size() - 1);
                    if (n.operator == 3) ret = n.value * ret;
                    else ret = n.value / ret;
                    queue.remove(queue.size() - 1);
                }
            } else if (c == ')') {
                index++;
                break;
            } else if (c == '*') {
                queue.add(new Node(ret, 3));
                index++;
            } else if (c == '/') {
                queue.add(new Node(ret, 4));
                index++;
            } else {
                ret = getNum();
                if (queue.size() > 0 && queue.get(queue.size() - 1).operator >=3) {
                    Node n = queue.get(queue.size() - 1);
                    if (n.operator == 3) ret = n.value * ret;
                    else ret = n.value / ret;
                    queue.remove(queue.size() - 1);
                }
            }
        }
        queue.add(new Node(ret,0));
        ret = 0;
        while(!queue.isEmpty()) {
            ret += (mul * queue.get(0).value);
            mul = queue.get(0).operator;
            queue.remove(0);
        }

        return ret;
    }

    public int calculate(String s) {
        index = 0;
        str = s;
        return cal();
    }
}

'''