# 105. Construct Binary Tree from Preorder and Inorder Traversal

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
#             / \
#            7   8
#             \
#              9
# pre(root, L, R) 1/2,4,5/3,6,7,9,8
# in(L, root, R)  4,2,5/1/3,7,9,6,8
#               L(4,2,5), R(3,7,9,6,8)
# Looking at preorder traversal, the first value (node 1) must be the root.
# Then, we find the index of root within in-order traversal, and split into two sub problems

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            print(f"ind={ind}, preorder={preorder}, inorder={inorder}")
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)

    # using deque
    def buildTree2(self, preorder, inorder):
        from collections import deque

        preorder = deque(preorder)
        print(f"preorder={preorder}, inorder={inorder}")
        return self.getTree(preorder, inorder)

    def getTree(self, preorder, inorder):
        print(f"preorder={preorder}, inorder={inorder}")
        if inorder:
            idx = inorder.index(preorder.popleft())
            print(f"idx={idx}, inorder[idx]={inorder[idx]}")
            root = TreeNode(inorder[idx])
            print(f"call left {root.val}")
            root.left = self.getTree(preorder, inorder[:idx])
            print(f"call right {root.val}")
            root.right = self.getTree(preorder, inorder[idx + 1:])
            return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
obj = Solution()

obj.inOrderTraversal(obj.buildTree(preorder, inorder))

# 106. Construct Binary Tree from Inorder and Postorder Traversal