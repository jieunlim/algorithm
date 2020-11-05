
# 230. Kth Smallest Element in a BST

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, arr):
        if not arr: return

        root = TreeNode(arr[0])

        dQ = deque()
        dQ.append(root)

        i = 1
        while dQ:
            node = dQ.popleft()

            if i < len(arr):
                if arr[i] is not None and node:  #is not None for dealing with '0' value
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] is not None and node:
                    node.right = TreeNode(arr[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        # self.inOrderT(root)
        return root

    def inOrderT(self, root):
        if root:
            self.inOrderT(root.left)
            print(root.val)
            self.inOrderT(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def helper(root):
            if not root:
                return

            # print(f"root={root.val}, {self.k}")

            helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.result = root.val
                return
            helper(root.right)

        self.result = -1
        self.k = k
        helper(root)
        return self.result

arr = [1,2,3,None,5,None,4]
arr = [1, None, 2, None, None, 3]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)