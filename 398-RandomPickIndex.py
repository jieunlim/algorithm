
# 398. Random Pick Index

# https://www.youtube.com/watch?v=A1iwzSew5QY
# Reservoir Sampling
# https://leetcode.com/problems/random-pick-index/discuss/88072/Simple-Reservoir-Sampling-solution

import random
class Solution2:
    def __init__(self, nums):
        self.nums = nums
        print(f"self.nums={self.nums}")

    def pick(self, target):
        res = None
        count = 0
        for idx, num in enumerate(self.nums):
            print(f"idx={idx}, num={num}")
            if num == target:
                count += 1
                print(f" count={count}")
                if random.randint(1, count) == count:
                    res = idx
                    print(f" res={res}")
        return res


obj = Solution2([1,2,3,3,3])
print(obj.pick(3))


# space O(N)
from collections import defaultdict
class Solution:
    def __init__(self, nums):
        self.nums = defaultdict(list)
        for idx, num in enumerate(nums):
            self.nums[num].append(idx)
        print(f"self.nums={self.nums}")
    #    {1: [0], 2: [1], 3: [2, 3, 4]})

    def pick(self, target):
        return random.choice(self.nums[target])


obj = Solution([1,2,3,3,3])
print(obj.pick(3))


# 528. Random Pick with Weight
