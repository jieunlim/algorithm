# 145. Binary Tree Postorder Traversal
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
    ####################

    def postorderTraversal2(self, root):
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)

        if not root: return None
        res = []
        helper(root)
        return res

    def postorderTraversal(self, root):
        if not root: return None
        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            # res.append(node.val)
            res.insert(0, node.val)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        # return res[::-1]
        return res

    def postorderTraversal22(self, root):
        if not root: return None
        res = []
        stack = []
        curNode = root

        while stack or curNode:
            if curNode:
                stack.append(curNode)
                res.insert(0, curNode.val)
                curNode = curNode.right
            else:
                node = stack.pop()
                curNode = node.left
        return res


# stack = [3]
# res = [2, 1, 3]

obj = Solution()
arr = [1, 2, 3]
r1 = obj.buildTree(arr)
obj.inOrderT(r1)

r = obj.postorderTraversal(r1)
print(f"rtn: {r}")
# obj.inOrderT(r)