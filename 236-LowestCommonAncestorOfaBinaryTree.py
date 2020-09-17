# 236. Lowest Common Ancestor of a Binary Tree

# O(N)
# O(h)- call stack, n==h worst case
#  what need to be happen to this node? root/left/right
# 1) find both 2)find either but not both

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor3(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root:
            return root

        if not root:
            return None

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r


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

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)


    def lowestCommonAncestor(self, root, p, q):

        def helper(node):

            if node == p or node == q:
                return node
            elif not node:
                return None

            L = helper(node.left)
            R = helper(node.right)

            if L and R:
                return node
            else:
                return L or R

        if not root: return None
        return helper(root)


    def lowestCommonAncestor1(self, root, p, q):
        # If looking for me, return myself
        if root == p or root == q:
            print(f"return root {root.val}")
            return root

        print(f"root.val={root.val}")

        left = right = None
        # else look in left and right child
        if root.left:
            print(f"  root.val = {root.val}, call left {root.left.val}")
            left = self.lowestCommonAncestor1(root.left, p, q)
        if root.right:
            print(f"  root.val = {root.val}, call right {root.right.val}")
            right = self.lowestCommonAncestor1(root.right, p, q)

        if left: print(f"  left={left.val}")
        if right: print(f"  right={right.val}")

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            print(f"  root.val = {root.val}, left {left}, and right {right}")
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            print(f"  root.val = {root.val}, left {left}, or right {right}")
            return left or right

    def lowestCommonAncestor2(self, root, p, q):
        if root == p or root == q:
            print(f"return root = {root.val}")
            return root
        elif not root:
            print(f"return None")
            return None

        print(f"root = {root.val}")
        print(f"call left  ")
        left = self.lowestCommonAncestor2(root.left, p, q)
        print(f"call right  ")
        right = self.lowestCommonAncestor2(root.right, p, q)

        if left: print(f"  left={left.val}")
        if right: print(f"  right={right.val}")

        if left and right:
            print(f"(AND) return root.val = {root.val}, left {left} and right {right}")
            return root

        print(f"(OR) return left {left} or right {right}")
        return left or right

    def lowestCommonAncestor3(self, root, p, q):
        # Stack for tree traversal
        stack = [root]
        # Dictionary for parent pointers
        parent = {root: None}
        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            print(f"node={node.val}")
            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # Ancestors set() for node p.
        ancestors = set()
        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]
        # The first ancestor of q which appears in
        # p’s ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

tlist = [1,2,3, 4,5,6]
tlist = [3,5,1,6,2,0,8,None,None,7,4]
tlist = [1,2,3,4,5,6,7]
obj = Solution()
root = obj.buildTree(tlist)
rtn = obj.lowestCommonAncestor(root, root.left.right, root.left.left)
print("rtn:", rtn.val)

# tlist = [6,2,8,0,4,7,9,None,None,3,5]
# obj = Solution()
# root = obj.buildTree(tlist)
# rtn = obj.lowestCommonAncestor(root, TreeNode(0), TreeNode(2))
# print(rtn.val)
print("====")
# tlist2 = [3,5,1,6,2,0,8,None,None,7,4]
# root2 = obj.buildTree(tlist2)
# rtn = obj.lowestCommonAncestor2(root2, TreeNode(5), TreeNode(4))
# print("return value = ", rtn)