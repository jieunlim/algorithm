
# 426. Convert Binary Search Tree to Sorted Doubly Linked List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root: return

        stack = []
        head, prev, cur = Node(-1), None, root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if not head.right:
                head.right = cur

            if prev:
                prev.right = cur
                cur.left = prev

            prev = cur
            cur = cur.right

        prev.right = head.right
        head.right.left = prev

        return head.right


    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = []
        cur = root
        head = Node(None)
        prev = None
        # iterative in order traversal
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            print(f"popped cur.val={cur.val}")
            # grab a reference to the first node
            if not head.right:
                head.right = cur
                if head.right: print(f"head.right={head.right.val}")

            # pred, succ links
            if prev:
                prev.right, cur.left = cur, prev
                if prev.right: print(f"prev.right={prev.right.val}")
                if cur.left: print(f"{cur.left.val}")

            prev = cur
            cur = cur.right
            if prev: print(f"prev={prev.val}")
            if cur: print(f"cur={cur.val}")

        # make circular
        prev.right = head.right
        head.right.left = prev

        return head.right