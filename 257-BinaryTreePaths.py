# 257. Binary Tree Paths

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

    # 257. Binary Tree Paths
    # time O(N)
    # space O(N)
    def binaryTreePaths(self, root):
        def helper(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    helper(root.left, path)
                    helper(root.right, path)

        paths = []
        helper(root, '')
        return paths

nums = [1,2,3,4,5]
obj = Solution()
r = obj.buildTree(nums)
print(obj.binaryTreePaths(r))