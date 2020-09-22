# 298. Binary Tree Longest Consecutive Sequence
# O(n)
# O(n)
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

    def longestConsecutive(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        maxVal = 0
        while stack:
            node, cnt = stack.pop()

            maxVal = max(maxVal, cnt)
            if node.left:
                if node.val + 1 == node.left.val:
                    c = cnt+1
                else:
                    c = 1
                stack.append((node.left, c))
            if node.right:
                if node.val + 1 == node.right.val:
                    c = cnt+1
                else:
                    c = 1
                stack.append((node.right, c))

        return maxVal

    def longestConsecutive2(self, root):
        self.maxVal = 0
        def helper(node, cnt):
            if not node: return 0

            self.maxVal = max(self.maxVal, cnt)

            if node.left:
                if node.val + 1 == node.left.val:
                    c = cnt+1
                else:
                    c = 1
                helper(node.left, c)

            if node.right:
                if node.val + 1 == node.right.val:
                    c = cnt+1
                else:
                    c = 1
                helper(node.right, c)


        if not root:
            return 0

        helper(root, 1)
        return self.maxVal

    def longestConsecutive3(self, root: TreeNode) -> int:
        self.longest = 0

        def helper(node):
            if not node: return 0

            l = helper(node.left)
            r = helper(node.right)

            ret = 1
            if node.left and node.val + 1 == node.left.val:
                ret = max(ret, l + 1)

            if node.right and node.val + 1 == node.right.val:
                ret = max(ret, r + 1)

            self.longest = max(self.longest, ret)
            return ret

        if not root: return 0
        helper(root)
        return self.longest

    # O(n)
    def longestConsecutive4(self, root: TreeNode) -> int:
        self.longest = 0

        def helper(node):
            if not node: return 0

            l = helper(node.left)
            r = helper(node.right)

            lVal, rVal = 1, 1
            if node.left and node.val + 1 == node.left.val:
                lVal = l + 1

            if node.right and node.val + 1 == node.right.val:
                rVal = r + 1

            self.longest = max(self.longest, lVal, rVal)
            return max(lVal, rVal)

        if not root: return 0
        helper(root)
        return self.longest

    def longestConsecutive5(self, root: TreeNode) -> int:

        def helper(node):
            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            if node.left and node.val + 1 == node.left.val:
                l += 1
            else:
                l = 1

            if node.right and node.val + 1 == node.right.val:
                r += 1
            else:
                r = 1

            maxLength = max(l, r)
            ret[0] = max(ret[0], maxLength)

            return maxLength

        ret = [0]
        helper(root)
        return ret[0]


arr = [1, None, 3, None, None,2,4, None, None, None, None, None, None, None, 5]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
print()
print(obj.longestConsecutive2(root))



# 250. Count Univalue Subtrees
# 508. Most Frequent Subtree Sum
# 543. Diameter of Binary Tree
# 1245. Tree Diameter
# 687. Longest Univalue Path
# 124. Binary Tree Maximum Path Sum
# Max Path Sum in a Grid
# 298. Binary Tree Longest Consecutive Sequence
# 549. Binary Tree Longest Consecutive Sequence II