class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def buildTree(self, nums):
        if not nums: return None

        root = TreeNode(nums[0])
        dq = deque([root])

        i = 1
        while dq:
            node = dq.popleft()

            if i < len(nums):
                if node and nums[i] is not None:
                    node.left = TreeNode(nums[i])
                    dq.append(node.left)
                else:
                    dq.append(None)
            i += 1

            if i < len(nums):
                if node and nums[i] is not None:
                    node.right = TreeNode(nums[i])
                    dq.append(node.right)
                else:
                    dq.append(None)
            i += 1

        self.inOrder(root)
        return root
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)


    def diameterNaryTree(self, root):

        self.maxLevel = float('-inf')

        def helper(node):

            if not node: return 0
            first = second = 0
            for c in node.children:
                depth = helper(c)
                if depth > first:
                    first, second = depth, first
                elif depth > second:
                    second = depth

            self.maxLevel = max(self.maxLevel, first + second)

            return first + 1

        helper(root)
        return self.maxLevel
nums = [1,2,3,None,5,4]
obj = Solution()
root = obj.buildTree(nums)
print(obj.binaryTreeRightSideView(root))