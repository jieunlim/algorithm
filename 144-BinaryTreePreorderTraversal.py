# 144. Binary Tree Preorder Traversal
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
                if arr[i] and node:
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] and node:
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

    def binaryTreeInorderTraversal(self, root):
        if not root: return []

        stack = [(root.val)]
        res = []
        while stack:
            nodeVal = stack.pop()

            if node.left: stack.append(node.left.val)

            res.append(node.val)

            if node.right: stack.append(node.right.val)
        return res

    def preorderTraversal2(self, root):
        if not root: return None

        stack = [root]
        res = []
        while stack :
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    def preorderTraversal1(self, root):
        from collections import deque

        if not root: return None

        dq = deque([root])
        res = []
        while dq:
            node = dq.popleft()

            res.append(node.val)
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)

        return res


    def preorderTraversal(self, root):

        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        if not root: return None
        res = []
        preorder(root)
        return res

obj = Solution()
arr = [1,2,3]
r1 = obj.buildTree(arr)
obj.inOrderT(r1)

r = obj.inorderTraversal(r1)
print(f"rtn: {r}")