
# 237. Delete Node in a Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):

        if node.next:
            node.val = node.next.val
            node.next = node.next.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(1)

l1.next = l2
l2.next = l3
l3.next = l4

# l1 = []
obj = Solution()
obj.deleteNode(l2)

pr = l1
while pr:
    print(pr.val)
    pr = pr.next

# 203. Remove Linked List Elements