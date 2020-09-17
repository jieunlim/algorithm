
# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/discuss/156321/Python-dfs-both-tree-at-same-time
#
# First, travel down the bigger tree via standard dfs,
# if we find node equal to the value of root of the smaller tree, compare the subtrees.
# We travel down both subtrees at the same time and if
# and only if every node is the same then we know we have found the right subtree.

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, alist):

        if not alist:
            return

        root = TreeNode (alist[0])
        myQ = deque()
        myQ.append(root)

        i = 1
        while len(myQ) > 0:
            node = myQ.popleft()

            if i < len(alist):
                if alist[i] is not None and node:
                    node.left = TreeNode(alist[i])
                    myQ.append(node.left)
                else:
                    myQ.append(None)

            i += 1

            if i < len(alist):
                if alist[i] is not None and node:
                    node.right = TreeNode(alist[i])
                    myQ.append(node.right)
                else:
                    myQ.append(None)

            i += 1

        self.preOrderTraversal(root)
        return root

    def preOrderTraversal(self, node):
        if node:
            print(node.val)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def isSubtree(self, s, t):

        def check(a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False

            if a.val != b.val:
                return False

            return check(a.left, b.left) and check(a.right, b.right)

        if not t: return True

        if not s: return False
        if s.val == t.val and check(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtree2(self, a, b):
        if not b:
            return True

        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False

            if root1.val != root2.val:
                return False

            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)

        def dfs(s, t):
            if not s:
                return False

            if s.val == t.val and checkTree(s, t):
                return True

            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(a, b)

s1 = [3,4,5,1,2]
s1 = [3,4,5,1,2,None,None,0]
t1 = [4,1,2]

obj = Solution()
s = obj.buildTree(s1)
t = obj.buildTree(t1)

print(obj.isSubtree(s, t))
# obj.preOrderTraversal(rtn)