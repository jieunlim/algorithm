# 136. Single Number

class Solution(object):
    # Approach 1: List Operation
    # 1) iterate over all the element in nums
    # 2) if some number in nums is new to array, append it
    # 3) is some number is already in the array, remove it
    # O(n), O(n)
    def singleNumber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
            print(f"no_duplicate_list={no_duplicate_list}")
        return no_duplicate_list.pop()

    # Approach 2: Hash Table
    # O(n), O(n)
    def singleNumber2(self, nums):
        from collections import defaultdict

        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        print(f"hash_table = {hash_table}")

        for n in hash_table:
            if hash_table[n] == 1:
                return n

    # Approach 3: Math
    # 2*(a+b+c) - (a+a+b+b+c) = c
    # O(n), O(n)
    def singleNumber3(self, nums):
        return 2*sum(set(nums)) - sum(nums)

    # Approach 4: Bit Manipulation
    # XOR 0 ^ 0 = 0, 1 ^ 1 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1
    # a ^ a = 0, a ^ 0 = a
    # a ^ a ^ b = 0 ^ b = b
    # [4,1,2,1,2] 0^4^1^2^1^2 = (0^4)^(1^1)^(2^2) = 4^0^0 = 4^0 = 4
    # O(n), O(1)
    def singleNumber4(self, nums):
        a = 0
        for n in nums:
            print(f"a={a}, n={n}")
            a ^= n
        return a

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber4(nums))

# 287. Find the Duplicate Number
