
# 94. Binary Tree Inorder Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, nums):
        from collections import deque

        if not nums: return

        dQ = deque()
        root = TreeNode(nums[0])
        dQ.append(root)
        lenN = len(nums)
        i = 1
        while len(dQ)>0:
            node = dQ.popleft()

            if i < lenN:
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < lenN:
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

    # 94. Binary Tree Inorder Traversal
    # recursively
    def inorderTraversal1(self, root):

        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)

        res = []
        helper(root, res)
        return res

    # iteratively
    def inorderTraversal(self, root):
        stack = []
        res = []
        curNode = root
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left

            curNode = stack.pop()
            res.append(curNode.val)
            curNode = curNode.right

        return res

    # def inorderTraversal2(self, root):
    #     ans = []
    #     stack = []
    #
    #     while stack or root:
    #         if root:
    #             stack.append(root)
    #             root = root.left
    #         else: #stack
    #             tmpNode = stack.pop()
    #             ans.append(tmpNode.val)
    #             root = tmpNode.right
    #
    #     return ans

nums = [2,1,3]
nums=[1,None,2,None,None,3]
obj = Solution()
r = obj.buildTree(nums)
print(obj.inorderTraversal2(r))