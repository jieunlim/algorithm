# 235. Lowest Common Ancestor of a Binary Search Tree
# O(N)
# O(h)- call stack, n==h worst case

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, alist):

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

        # self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)

    # Binary Search Tree
    # All of the nodes' values will be unique.
    # p and q are different and both values will exist in the BST.

    # BST
    # Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
    # Right subtree of a node N contains nodes whose values are greater than node N's value.
    # Both left and right subtrees are also BSTs.
    # Recursive approach
    # Find the Lowest Common Ancestor
    def lowestCommonAncestor(self, root, p, q):

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor2(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

tlist = [6,2,8,0,4,7,9,None,None,3,5]
obj = Solution()
root = obj.buildTree(tlist)
rtn = obj.lowestCommonAncestor(root, TreeNode(0), TreeNode(2))
print(rtn.val)
print("====")
tlist2 = [3,5,1,6,2,0,8,None,None,7,4]
root2 = obj.buildTree(tlist2)
rtn = obj.lowestCommonAncestor2(root2, TreeNode(5), TreeNode(4))
print("return value = ", rtn)