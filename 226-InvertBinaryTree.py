# 226. Invert Binary Tree
# Invert a binary tree.

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
        root = TreeNode(nums[0])
        dQ = deque()
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

    def invertTree(self, root):

        if not root: return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree2(self, root):
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree3(self, root):
        from collections import deque
        if not root: return None
        dQ = deque()
        dQ.append(root)
        while len(dQ) > 0:
            node = dQ.popleft()
            node.left, node.right = node.right, node.left
            if node.left: dQ.append(node.left)
            if node.right: dQ.append(node.right)
        return root

nums = [1,2,3]
nums = [1,2,3,4,5,6,7]
nums = [1,2]
obj = Solution()
root = obj.buildTree(nums)
print(f"return: ")
obj.inOrderTraversal(obj.invertTree2(root))


