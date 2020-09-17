# 103. Binary Tree Zigzag Level Order Traversal

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, alist):

        if not alist:
            return

        root = TreeNode (alist[0])
        myQ = deque()
        myQ.append(root)

        i = 1
        while len(myQ) > 0:
            node = myQ.popleft()

            if i < len(alist):
                if alist[i] is not None and node:
                    node.left = TreeNode(alist[i])
                    myQ.append(node.left)
                else:
                    myQ.append(None)

            i += 1

            if i < len(alist):
                if alist[i] is not None and node:
                    node.right = TreeNode(alist[i])
                    myQ.append(node.right)
                else:
                    myQ.append(None)

            i += 1

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)

    # time O(N), N is the number of nodes in the tree
    # space O(N)
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/34152/Short-and-clear-python-code
    def zigzagLevelOrder(self, root):
        import collections
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            print(f"r={r}")
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
                    print(f"r={r}, len(res) % 2={len(res) % 2}")

            r = r[::-1] if len(res) % 2 else r
            if r:
                res.append(r)
        return res

alist = [3,9,20,None,None,15,7]

obj = Solution()
root = obj.buildTree(alist)
print(obj.zigzagLevelOrder(root))
