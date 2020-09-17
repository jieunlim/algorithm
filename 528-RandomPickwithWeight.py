# 528. Random Pick with Weight
# random, binary search


class Solution:
    # [1,3,4,4]
    # [0, 1,1,1,2,2,2,2,3,3,3,3]
    # [1,4,8,12]

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:

        seed = random.randint(1, self.w[-1])
        start, end = 0, len(self.w) - 1
        while start < end:
            mid = start + (end - start) // 2
            if self.w[mid] < seed:
                start = mid + 1
            else:
                end = mid
        return start



# sol 1
# [1,3,4,4]
# 0,1,2,3 index
# Generate an array with x occurences of each index where x is the weight
# new array - [0,1,1,1,2,2,2,2,3,3,3,3]

# sol 2
#  [1,4,8,12] -> the final index will have the total weight
#  1. Generate a prefix sum of the weights (O(N)
#  2. Generate a random number between 0 and length(array)-1
#  3. Binary search for the random number O(logN)

# 398. Random Pick Index

class Solution:
    def __init__(self, w):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i-1]
        self.s = self.w[-1]

    def pickIndex(self):
        seed = random.randint(1, self.s)
        l, r = 0, self.n - 1
        while l < r:
            mid = l + (r-l)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l

# for the array of {1, 3, 4, 6}
# the pickIndex() call will have 1/(1+3+4+6) = 1/14 = ~7% chance of picking index 0;
# 3/14 = 21% change of picking index 1;
# 4/14 = 29% change of picking index 2;
# and 6/14 = 43% of picking index 3.

import itertools, bisect, random
class Solution2:
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

# https://leetcode.com/problems/random-pick-with-weight/discuss/154076/Python-binary-search-solution
# binary search
# Generate a prefix sum of the weights; then generate a random integer;
# after that, search for the indes using binary search, O(nlogn)
class Solution3:

    def __init__(self, w):
        self.w = w
        self.n = len(w)
        for i in range(1,self.n):
            self.w[i] += self.w[i-1]
        print(f"w={w}")
        self.s = self.w[-1]
        print(f"self.w={self.w}, w={w}, self.n={self.n}, self.s={self.s}")
        print(f"{id(self.w)}, {id(w)}")

    def pickIndex(self):
        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        print(f"seed={seed}, l={l}, r={r}")
        while l<r:
            mid = (l+r)//2
            print(f"mid = {mid}, l={l}, r={r}, seed={seed}, self.w={self.w}")
            if seed <= self.w[mid]:
                r = mid
                print(f"r={r}")
            else:
                l = mid+1
                print(f"l={l}")
        print(f"return l={l}")
        return l

w = [3,10,7]
w=[1,3,4,4]
obj = Solution3(w)
print(obj.pickIndex())

'''
528. Random Pick with Weight
class Solution0528 {
    int[] range;
    int max;
    public Solution0528(int[] w) {
        range = new int[w.length + 1];
        int sum = 0;
        range[0] = 0;
        for (int i=1; i<=w.length; i++) {
            sum+=w[i-1];
            range[i] = sum;
        }
        max = sum;
    }

    public int pickIndex() {
        int l = 1, r = range.length - 1;
        int num = (int)(Math.random() * max) + 1;
        int mid = (l+r) / 2;;
        while(l<r) {
            if (range[mid] < num) l = mid + 1;
            else if (range[mid - 1] >= num) r = mid - 1;
            else return mid - 1;
            mid = (l+r) / 2;
        }
        return mid - 1;
    }
}
'''