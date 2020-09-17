# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
# https://www.youtube.com/watch?v=MRe3UsRadKw&feature=emb_logo
# time O(n)
# space O(1) 0 iterative, O(n) -recursion stack
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList2(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev

        if node: print(f"node={node.val}")
        if prev: print(f"prev={prev.val}")
        n = node.next
        if n: print(f"n={n.val}")
        node.next = prev
        if node.next: print(f"node.next.val={node.next.val}")
        return self._reverse(n, node)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3
obj = Solution()
r = obj.reverseList(l1)

pr = r
while pr:
    print(pr.val)
    pr = pr.next

# 92. Reverse Linked List II
# 156. Binary Tree Upside Down
# 234. Palindrome Linked List