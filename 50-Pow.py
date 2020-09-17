
# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
class Solution(object):
    def myPow(self, a, b):
        if b < 0:
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)

    def helper(self, a, b):
        print(f"a={a}, b={b}")

        if b == 0: return 1

        half = self.helper(a, b // 2)

        print(f" half={half} a={a}, b={b}")
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a


a=2.10000
b = 3
obj = Solution()
print(obj.myPow(a, b))