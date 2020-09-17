# 1512. Number of Good Pairs
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # {1:3, 2:1, 3:1}
        from collections import defaultdict
        dic = defaultdict(int)

        result = 0
        for n in nums:
            result += dic[n]
            dic[n] += 1

        return result

    #    [1,2,3,1,1,3]
# result =0 0 0 1 3 4

    def numIdenticalPairs2(self, nums: List[int]) -> int:
        # {1:3, 2:1, 3:1}
        from collections import defaultdict
        dic = defaultdict(int)

        result = 0
        for n in nums:
            dic[n] += 1

        print(dic.values())
        print(list(dic.values()))
        for d in list(dic.values()):
            if d > 1: result += d*(d-1)//2

        return result

nums = [1,2,3,1,1,3]
obj = Solution()
print(obj.numIdenticalPairs2(nums))
# 2 - (1) 1
# 3 - (2+1) 3
# 4- (3+2+1) 6
# 5-(4+3+2+1) 10
# n(n-1)//2
