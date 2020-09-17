
# 1234. Replace the Substring for Balanced String

# sliding window 방법, 윈도우 바깥쪽을 count해서 2 이하일때까지만.
# 다른 방법은,
# 1. 완쪽부터 스캔, 오른쪽부터 스캔 2 이하일때까지
# 2. 오른쪽부터, 왼쪽
# 3. 왼쪽 오른쪽 동시 스캔
# 셋 중 가장 min 값 구하면 되지만 구현이 복잡.

import collections
class Solution(object):
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        print(f"count={count}, n={n}")
        i = 0
        for j, c in enumerate(s):
            print(f"j={j}, c={c}")
            count[c] -= 1
            print(f"count={count}")
            print(all(n / 4 >= count[c] for c in 'QWER'))
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                print(f"    while i={i}, j={j} ")
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
                print(f"        res={res}, count={count}, i={i}")
        return res

s = "QWER"
s = "QQQW"
# s = "QQQQ"
s="WWEQERQWQWWRWWERQWEQ"
# s="QQQWEEER"
obj = Solution()
print(obj.balancedString(s))