# 282. Expression Add Operators
# https://youtu.be/uhZeoivB7_4
# 4 choices at N-1 locations -> total possibilities 4^(N-1)
# O(N) to evaluate one possibility
# Time complexity O(N*4^(N-1))
# Space - O(N) for recursion stack, for path
from typing import List
def addOperators(num: 'str', target: 'int') -> 'List[str]':
    def helper(idx, candidate, total, prev):
        if idx == len(num) and total == target:
            res.append(candidate)
            return

        for j in range(idx + 1, len(num) + 1):
            s = num[idx:j]
            d = int(s)

            # if s != '0' and num[idx] == '0': continue
            if len(s) > 1 and s[0] == '0':
                continue #'105' -> '05' is not valid

            if not candidate:
                helper(j, s, d, d)
            else:
                helper(j, candidate + '+' + s, total + d, d)
                helper(j, candidate + '-' + s, total - d, -d)
                helper(j, candidate + '*' + s, total - prev + prev * d, prev * d)

    res = []
    helper(0, '', 0, 0)
    return res


num = '00'
target = 0
num='105'
target = 5
# num='123'
# target=6
# num = "3456237490"
# target = 9191  #[]
print(addOperators(num, target))