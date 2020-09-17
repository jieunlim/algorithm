# 8. String to Integer (atoi)

# get rid of all leading whitespaces
# sign of the number
# overflow

def myAtoi(str):

    if not str: return 0

    sign, num= 1, 0
    tStr = ""

    # tStr = str.strip()
    i = 0
    while i < len(str):
        if len(tStr) > 0 and str[i] == " ":
            break
        elif str[i] == " ":
            i += 1
            continue
        else:
            tStr += str[i]
            print(f"tStr={tStr}")
        i += 1

    if not tStr: return 0

    i = 0
    if tStr[0] in ['-', '+']:
        if tStr[0] == '-':
            sign = -1
        i += 1

    while i < len(tStr) and tStr[i].isdigit():
        num = num * 10 + ord(tStr[i]) - ord('0')
        i += 1

    #return sign * num
    return max(-2 ** 31, min(sign * num, 2 ** 31 - 1))

# str = "-22 a"
# str="words and 987"
# str="-91283472332"
str="3.14159"
str="+1"
str="+-2"
str=""
str=" a-0  /"
# str=" "
# str="   +0 123"
# str="4193 with words"
print("result:", myAtoi(str))




# math, string
class Solution(object):
    def myAtoi(self, s):

        ###better to do strip before sanity check (although 8ms slower):
        # ls = list(s.strip())
        # if len(ls) == 0 : return 0
        if len(s) == 0: return 0
        ls = list(s.strip())

        print(f"ls={ls}")
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            print(f"ls={ls}")
            del ls[0]
            print(f"ls={ls}")
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


# s=" -42"
# s="Word 412"
# s="3281 with"
# s="-91283472332"
# s="3.14159"
s="+-2"
str="   +0 123"
obj = Solution()
# print(obj.myAtoi(s))