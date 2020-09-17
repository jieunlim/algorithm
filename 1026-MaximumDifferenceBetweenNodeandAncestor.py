# 1026. Maximum Difference Between Node and Ancestor
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
                if arr[i] is not None and node:
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

    def maxAncestorDiff(self, root):

        def helper(node, minVal, maxVal):

            if not node:
                return maxVal - minVal

            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            return max(helper(node.left, minVal, maxVal), helper(node.right, minVal, maxVal))

        if not root: return 0
        return helper(root, float('inf'), float('-inf'))

obj = Solution()
arr = [6,2,9]
arr = [8,3,10,1,6,None,14,None,None,4,7,13] #7
root = obj.buildTree(arr)
obj.inOrderT(root)
print()
r = obj.maxAncestorDiff(root)
print(r)