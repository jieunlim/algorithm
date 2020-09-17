# 314. Binary Tree Vertical Order Traversal

# https://leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/76420/Vertical-Order-in-Python
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

    # BFS + mapping
    # time O(N)
    # space O(N)
    def verticalOrder(self, root):
        """
        this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        - for the left  node, you set its index as index - 1
        - for the right node, you set its index as index + 1
        - use queue to loop through all the nodes in a tree
        - set index as a key to the hashmap() and value as a list of vals
        - add node.data into hashmap() with index as a key
        - keep track of min and max index and store into solution list and return it
        """
        if not (root): return []

        res, MIN, MAX = [], 0, 0
        table = {}
        queue = [(root, 0)]

        print(f"queue={queue}")
        while queue:

            # order matters
            node, index = queue.pop(0)
            if index not in table:
                table[index] = [node.val]
            else:
                table[index].append(node.val)

            print(f"table={table}")
            # left comes first.
            if node.left:
                MIN = min(MIN, index - 1)
                queue.append((node.left, index - 1))
            if node.right:
                MAX = max(MAX, index + 1)
                queue.append((node.right, index + 1))

        for i in range(MIN, MAX + 1):
            res.append(table[i])

        return res


alist = [3,9,20,None,None,15,7]

obj = Solution()
root = obj.buildTree(alist)
print(obj.verticalOrder(root))



# 102. Binary Tree Level Order Traversal

# 987. Vertical Order Traversal of a Binary Tree