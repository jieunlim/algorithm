
# 415. Add Strings
# time complexity O(max(N1, N2))
# space complexity O(max(N1, N2))
# https://leetcode.com/problems/add-strings/discuss/90474/straightforward-python-solution
class Solution(object):

    def addStrings(self, num1, num2):
        res = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        ordZero = ord('0')
        while i >= 0 or j >= 0 or carry > 0:
            n1 = ord(num1[i]) - ordZero if i >= 0 else 0
            n2 = ord(num2[j]) - ordZero if j >= 0 else 0
            print(f"n1={n1}, n2={n2}, carry={carry}")
            total = n1 + n2 + carry
            res.append(str(total % 10))  #res.insert(0, str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1

        return "".join(res[::-1])  #"".join(res)

    def addStrings2(self, num1, num2):

        n1, n2 = 0, 0
        for i in range(len(num1)):
            print(f"i={i} n1 * 10={n1 * 10}, ord(num1[i]) ={ord(num1[i])}")
            n1 = n1 * 10 + ord(num1[i]) - 48
            print(f"n1={n1}")
        for i in range(len(num2)):
            print(f"i={i} n2 * 10={n2 * 10}, ord(num2[i]) ={ord(num2[i])}")
            n2 = n2 * 10 + ord(num2[i]) - 48
            print(f"n2={n2}")
        return str(n1 + n2)

    def addStrings3(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]

    def addBinary3(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        # print(x, y)
        while y:
            x, y = x ^ y, (x & y) << 1
            # print(bin(x), bin(y))

        return bin(x)[2:]
num1="123"
num2="3"
obj = Solution()
print(obj.addStrings(num1, num2))