# 19. Remove Nth Node From End of List

# O(L) - the list of L nodes
# O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next
        print(f"fast={fast.val}")
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        print(f"fast={fast.val}, slow={slow.val}")
        slow.next = slow.next.next
        return dummy.next

head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

obj = Solution()
n=5
r = obj.removeNthFromEnd(head, n)
pr = r
while pr:
    print(pr.val)
    pr= pr.next