# 287. Find the Duplicate Number
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.

# Note
# 1) You must not modify the array (assume the array is read only).
# 2) You must use only constant, O(1) extra space.
# 3) Your runtime complexity should be less than O(n2).
# 4) There is only one duplicate number in the array, but it could be repeated more than once.

# using sort - have to modify the array, using set - extra space
# two conditions : read only input array, O(1) space --> Floyd's tortoise and hare algorithm
# 141, 142 Linked List Cycle

class Solution:
    # O(n), O(1)
    # https://leetcode.com/problems/find-the-duplicate-number/discuss/72852/Python-same-solution-as-142-Linked-List-Cycle-II
    def findDuplicate(self, nums):
        slow = fast = finder = 0
        print(f"nums={nums}")
        while True:
            print(f"slow={slow}, fast={fast}")
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(f"  slow={slow}, fast={fast}")

            if slow == fast:
                print(f"    slow={slow}, finder={finder}")
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                    print(f"        slow={slow}, finder={finder}")

                print(f" return finder={finder}")
                return finder
        return -1

nums = [1,3,4,2,2]
# nums=[1,7,5,2,3,6,6,4]
obj = Solution()
print(obj.findDuplicate(nums))

# 136. Single Number
# 142. Linked List Cycle II
