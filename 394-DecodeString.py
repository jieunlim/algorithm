# 394. Decode String

class Solution:
    # def decodeString2(self, s):
    #     if not s: return
    #     res = ''
    #
    #     splitStr = s.split(']')
    #     print(f"splitStr={splitStr}")
    #     for i in range(len(splitStr)-1):
    #         items = splitStr[i].split('[')
    #         print(f"items={items}")
    #         num = int(items[0])
    #         for i in range(num):
    #             res += items[1]
    #
    #     res += splitStr[-1]
    #     return res

    # https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            print(f"c={c}")
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
                print(f"stack={stack}, curString={curString}, curNum={curNum}")
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
                print(f"num={num}, prevString={prevString}, curString={curString}")
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
                print(f"curNum={curNum}")
            else:
                curString += c
                print(f"curString={curString}")
        return curString

    def decodeString2(self, s):
        stack, curString, curNum= [], '', 0
        for c in s:
            print(f"c={c}")
            if c == '[':
                stack.append((curString,curNum))
                curString = ''
                curNum = 0
                print(f"stack={stack}, curString={curString}, curNum={curNum}")
            elif c == ']':
                prevString, num = stack.pop()
                curString = prevString + num * curString
                print(f"num={num}, prevString={prevString}, curString={curString}")
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
                print(f"curNum={curNum}")
            else:
                curString += c
                print(f"curString={curString}")
        return curString
s = "3[a]2[bc]"
# s = "2[abc]3[cd]ef"
# s="3[a2[c]]"
# s = "100[leetcode]"  #test -->  curNum = curNum * 10 + int(c)
obj = Solution()
print(obj.decodeString2(s))