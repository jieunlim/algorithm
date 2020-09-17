# 104. Maximum Depth of Binary Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def buildTree(self, nums):

        if not nums: return

        lenNums = len(nums)
        dQ = deque()
        root = TreeNode(nums[0])
        dQ.append(root)

        i = 1
        while len(dQ) > 0:
            node = dQ.popleft()

            if i < lenNums:
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1

            if i < lenNums:
                if nums[i] and node:
                    node.right = TreeNode(nums[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)

    # O(n), O(n)
    def maxDepth(self, root):

        if not root:
            return 0

        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)

        return max(L, R) + 1

    # def maxDepth(self, root):
    #
    #     if not root:
    #         return 0
    #
    #     # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #     print(f"root = {root.val}")
    #     l = self.maxDepth(root.left)
    #     print(f"l={l}")
    #     r = self.maxDepth(root.right)
    #     print(f"r={r}")
    #     rtn = 1 + max(l, r)
    #     print(f"rtn = {rtn}, root = {root.val}")
    #     return rtn

    # Iteration, stack
    # O(n), O(n)
    def maxDepth2(self, root):
        if not root: return 0
        stack = []
        stack.append((1, root))

        depth = 0
        while stack:
            curDepth, node = stack.pop()
            if root:
                depth = max(depth, curDepth)
                if node.left: stack.append((curDepth + 1, node.left))
                if node.right: stack.append((curDepth + 1, node.right))

        return depth

nums = [1,2, 3, 4]

obj = Solution()
root = obj.buildTree(nums)
print()
print(obj.maxDepth(root))