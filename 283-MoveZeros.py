
# 283. Move Zeroes
# in-place
# minimize the total number of operations

# A two-pointer approach could be helpful here.
# The idea would be to have one pointer for iterating the array
# and another pointer that just works on the non-zero elements of the array.

# O(N), space O(1)
def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
        print(f"i={i}")
        if nums[i] != 0:
            print(f"pos={pos}, i={i}, nums={nums}")
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

nums=[0,1,0,3,12]
# nums=[0,0,0, 1,2]
moveZeroes(nums)
print(nums)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        p = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        for i in range(p, len(nums)):
            nums[i] = 0

#         0, 1, 0, 3, 12
#         p  i
#         1, 3, 12, p  i...


#         nums[i] != 0