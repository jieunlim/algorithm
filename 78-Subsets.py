# 78. Subsets
# https://youtu.be/bGC2fNALbNU

# https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).

class Solution:
    # DFS recursively
    # time O(2^N) N is total number of element
    # space O(N*2^N)
    def subsets1(self, nums):

        def helper(idx, path):
            res.append(path)

            # if idx >= len(nums): return

            for s in range(idx, len(nums)):
                helper(s + 1, path + [nums[s]])

        res = []
        helper(0, [])
        return res

    # time O(N*2^N)
    # space O(N*2^N)
    def subsets(nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            print(f"k={k}, first={first}, curr={curr}")
            if len(curr) == k:
                output.append(curr[:])
                print(f"output={output}")
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            print(f"k={k}")
            backtrack()
        return output

    # Bit Manipulation
    def subsets2(self, nums):
        res = []
        nums.sort()
        print(1 << len(nums))
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                print(f"i={i}, j={j}, {1 << j}, {bin(1 << j)}, {i & 1 << j}")
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
                    print(f"i={i}, j={j}, tmp={tmp}")
            res.append(tmp)
        return res

    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

    def subsets4(nums):
        res = [[]]
        for num in sorted(nums):
            r = []
            print(f"res={res}")
            for item in res:
                r += [item + [num]]
                print(f"r={r}")
            res += r
            # res += [item + [num] for item in res]
        return res

    def subsets3(self, nums):
        # return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])
        a = [[]]
        for i in nums:
            for j in range(len(a)):
                b = a[j].copy()
                b.append(i)
                a.append(b)
        return a
nums=[1,2,3]
obj = Solution()
print(obj.subsets2(nums))


# 90. Subsets II