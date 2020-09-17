# 98. Validate Binary Search Tree

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

    # Recursion
    def isValidBST(self, root):

        def isValid(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            print(f"node={node.val}")

            if node.val <= lower or node.val >= upper:
                return False

            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)

        return isValid(root)

    # DFS
    def isValidBST2(self, root):

        if not root: return True
        lower = float('-inf')
        upper = float('inf')

        stack = [(root, lower, upper)]

        while stack:
            node, lower, upper = stack.pop()

            if node.val <= lower or node.val >= upper:
                return False

            if node.right: stack.append((node.right, node.val, upper))
            if node.left: stack.append((node.left, lower, node.val))

        return True

    # inorder traversal : Left < root < right
    def isValidBST3(self, root):

        if not root: return True
        inorder = float('-inf')
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= inorder:
                return False

            inorder = root.val
            root = root.right

        return True


obj = Solution()
arr = [5, 1, 6]
root = obj.buildTree(arr)
obj.inOrderT(root)

r = obj.isValidBST3(root)
print(f"rtn : {r}")

'''

    # inorder traversal
    # O(n), O(n)
    def isValidBST(self, root):
        def inOrder(root, output):
            if root is None:
                return

            inOrder(root.left, output)
            output.append(root.val)
            inOrder(root.right, output)

        output = []
        inOrder(root, output)
        print(f"output={output}")
        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    # inorder traversal
    # O(n), O(1)
    # https://leetcode.com/problems/validate-binary-search-tree/discuss/32153/Python-version-based-on-inorder-traversal
    def isValidBST2(self, root: TreeNode) -> bool:

        self.lastelement = float("-inf")
        self.result = True

        def helper(node):
            if not node:
                return
            print(f"node={node.val}, self.lastelement={self.lastelement}")
            helper(node.left)
            print(f"*node={node.val}, self.lastelement={self.lastelement}")
            if node.val <= self.lastelement:
                self.result = False
                return
            else:
                self.lastelement = node.val
            helper(node.right)

        helper(root)
        return self.result


'''
# def isValidBST2(self, root, lessThan=float('inf'), largerThan=float('-inf')):
#     if not root:
#         return True
#     if root.val <= largerThan or root.val >= lessThan:
#         return False
#     return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
#            self.isValidBST(root.right, lessThan, max(root.val, largerThan))

# def isValidBST(self, root):
#     def check_bst(node, left, right):
#         if not node:
#             return True
#
#         if not left < node.val < right:
#             return False
#
#         return (check_bst(node.left, left, node.val)
#                 and check_bst(node.right, node.val, right))
#
#     return check_bst(root, float("-inf"), float("inf"))