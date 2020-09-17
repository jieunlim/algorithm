
# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1

        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x //= 10
            print(f"result={result}, x={x}")

        return 0 if result > pow(2, 31) else result * symbol


x=123
obj = Solution()
print(obj.reverse(x))

