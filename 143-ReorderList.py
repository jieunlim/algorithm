
# 143. Reorder List

# time O(N)
# space O(1)

# Middle of the Linked List.
# Reverse Linked List.
# Merge Two Sorted Lists.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):

        if not head: return

        # find a middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        print(f"second = {second.val}")
        # reverse the second part of the list
        prev = None
        while second:
            cur = second
            second = second.next
            cur.next = prev
            prev = cur

        l1 = head
        l2 = prev

        # print(f"l1 = {l1.val}, l2={l2.val}")
        # merge two sorted lists
        while l1 and l2:
            tmp = l1.next
            l1.next = l2
            l1 = tmp
            tmp = l2.next
            l2.next = l1
            l2 = tmp

        return head


head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

obj = Solution()
r = obj.reorderList(head)

pr = r
while pr:
    print(pr.val)
    pr = pr.next