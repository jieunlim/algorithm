
# 67. Add Binary
# time O(M+N)
# space O(max(M, N)) to keep the answer
class Solution:
    def addBinary2(self, a, b):
        a, b = list(a), list(b)

        carry, res = 0, []
        while a or b or carry:
            n1 = ord(a.pop()) - ord('0') if a else 0
            n2 = ord(b.pop()) - ord('0') if b else 0

            carry, val = divmod(n1 + n2 + carry, 2)
            res.insert(0, val)

        return "".join([str(v) for v in res])

    # for answer(XOR)
    # 1, 1 -> 0 (1^1)
    # 1, 0/ 0, 1-> 1 (1^0)
    # for carry
    # 1, 1 -> 10 (1^1 << 1)
    # 1, 0/ 0,1 -> 00
    def addBinary(self, num1, num2):

        a, b = int(num1, 2), int(num2, 2)

        while b:
            answer = a ^ b
            carry = (a & b) << 1
            a, b = answer, carry

        return bin(a)[2:]

    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            print(f"x={bin(x)}, y={bin(y)}")
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print(f"answer={bin(answer)}, carry={carry}, x={bin(x)}, y={bin(y)}")
            print(type(bin(x)))
        return bin(x)[2:]


######################################
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        n1 = n2 = carry = 0
        res = []
        # result = ''
        while len(a) > 0 or len(b) > 0 or carry:
            n1 = ord(a.pop()) - ord('0') if len(a) > 0 else 0
            n2 = ord(b.pop()) - ord('0') if len(b) > 0 else 0

            s = n1 + n2 + carry
            tmp = s%2
            carry = s//2

            # if s == 3:
            #     carry = 1
            #     tmp = 1
            # elif s == 2:
            #     carry = 1
            #     tmp = 0
            # else:
            #     carry = 0
            #     tmp = s
            res.append(tmp)
            # result += str(tmp)
            # print(res, tmp, len(a), len(b), carry, n1, n2)
        return "".join([str(c) for c in res])[::-1]
        # return result[::-1]

    def addBinary2(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry //= 2

        return result[::-1]


a="11"
b="1"
a = "1010"
b = "1011"
obj = Solution()
print(obj.addBinary(a, b))

# 415. Add Strings


'''

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        print(x, y)
        while y:
            print(f"x={x}, y={y}")
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print(f"answer={answer}, carry={carry}, x={x}, y={y}")
        return bin(x)[2:]

    def addBinary2(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        print(f"n={n}, a={a}, b={b}")

        for i in range(n - 1, -1, -1):
            print(f"i={i}, a[i]={a[i]}, b[i]={b[i]}")
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            print(f" carry={carry}")
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

            print(f"answer={answer}, carry={carry}")
        if carry == 1:
            answer.append('1')
        answer.reverse()

        print(f"answer={answer}")
        return ''.join(answer)

a="11"
b="1"
obj = Solution()
# print(obj.addBinary2(a,b))

'''