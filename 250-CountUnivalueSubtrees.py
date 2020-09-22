# 250. Count Univalue Subtrees

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
                if arr[i]is not None and node:  #is not None for dealing with '0' value
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

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        #         self.ans = 0
        #         def recurse(node, parent):
        #             if not node:
        #                 return True
        #             left = recurse(node.left, node.val)
        #             right = recurse(node.right, node.val)
        #             if left and right:
        #                 self.ans += 1
        #             return left and right and node.val == parent
        #         recurse(root, None)
        #         return self.ans

        self.count = 0

        def helper(root):
            if not root:
                return
            left = helper(root.left)
            right = helper(root.right)
            if (not left or left == root.val) and (not right or right == root.val):
                self.count += 1
                return root.val

            # If current tree is not univalued, the parent tree cannot be univalued either.
            # So we return a value that the parent tree's root node can never match.
            return '#'

        helper(root)
        return self.count

obj = Solution()
arr = [5,1,5,5,5,None,5]  #4
root = obj.buildTree(arr)
obj.inOrderT(root)
print()
print(obj.countUnivalSubtrees(root))



# 250. Count Univalue Subtrees
# 508. Most Frequent Subtree Sum
# 543. Diameter of Binary Tree
# 1245. Tree Diameter
# 687. Longest Univalue Path
# 124. Binary Tree Maximum Path Sum
# Max Path Sum in a Grid
# 298. Binary Tree Longest Consecutive Sequence
# 549. Binary Tree Longest Consecutive Sequence II