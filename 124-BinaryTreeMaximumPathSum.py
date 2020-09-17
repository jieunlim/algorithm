# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, nums):
        if not nums: return None

        root = TreeNode(nums[0])
        idx = 1
        dq = deque([root])

        while dq:
            node = dq.popleft()

            if idx < len(nums):
                if nums[idx] is not None and node:
                    node.left = TreeNode(nums[idx])
                    dq.append(node.left)
                else:
                    dq.append(None)
            idx += 1
            if idx < len(nums):
                if nums[idx] is not None and node:
                    node.right = TreeNode(nums[idx])
                    dq.append(node.right)
                else:
                    dq.append(None)
            idx += 1

        self.inOrder(root)
        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

    # O(N)
    # O(H)
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def helper(node):
            if not node: return 0
            print(f"node={node.val}")
            left = max(0, helper(node.left))
            print(f"left={left}")
            right = max(0, helper(node.right))
            print(f"right={right}")

            self.maxSum = max(self.maxSum, node.val + left + right)
            print(f"maxSum = {self.maxSum}, return = {node.val + max(left, right)}")
            return node.val + max(left, right)

        helper(root)
        return self.maxSum

nums = [-4,-2,-3]
nums = [2, -1] #2
obj = Solution()
root = obj.buildTree(nums)
print("rtn:", obj.maxPathSum(root))