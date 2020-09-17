# 142. Linked List Cycle II
# Given a linked list, return the node where the cycle begins
# Note: Do not modify the linked list.
# Follow-up:
# Can you solve it without using extra space?

# 141 description
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Hash
    # Leetcode Solution Approach 1
    def detectCycle(self, head):
        dict = set()
        while head:
            if head in dict:
                return head
            else:
                dict.add(head)
            head = head.next
        return None

    # Floyd's Cycle Detection Alogrithm or Tortoise and Hare Algorithm
    # Solution Approach2
    def detectCycle2(self, head):
        if not head: return None

        fast = slow = ptr = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print(f"slow.val={slow.val}, fast.val={fast.val}")
                while slow != ptr:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None

head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

head.next = l2
l2.next = l3
l3.next = l2
obj = Solution()
# print(obj.detectCycle(head))

r = obj.detectCycle2(head)
print(r.val)

