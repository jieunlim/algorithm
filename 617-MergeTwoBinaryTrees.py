# 617. Merge Two Binary Trees

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
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

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)

    # DFS recursive
    # O(N), O(1)
    def mergeTrees(self, t1, t2):

        if not t1: return t2
        if not t2: return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    # DFS stack
    def mergeTrees2(self, t1, t2):
        if t1 is None:
            return t2

        stack = []
        stack.append((t1, t2))
        while stack:
            t = stack.pop()
            if t[1] is None:
                continue
            print(f"  t[0].val={t[0].val}, t[1].val={t[1].val}")
            t[0].val += t[1].val

            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))

            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1

    # BFS, queue
    def mergeTrees3(self, t1, t2):
        import collections

        if t1 is None:
            return t2

        myQ =  collections.deque()
        myQ.append((t1,t2))
        while myQ:
            t = myQ.popleft()
            if t[1] is None:
                continue
            print(f"  t[0].val={t[0].val}, t[1].val={t[1].val}")
            t[0].val += t[1].val

            if t[0].left is None:
                t[0].left = t[1].left
            else:
                myQ.append((t[0].left, t[1].left))

            if t[0].right is None:
                t[0].right = t[1].right
            else:
                myQ.append((t[0].right, t[1].right))
        return t1


nums1 = [1,2,3,4,5, None, 20]
nums2=[6,7,8,None,9,10, 30]
# nums1=[1,3]
# nums2=[2,1,5]
obj = Solution()
t1= obj.buildTree(nums1)
t2= obj.buildTree(nums2)
r = obj.mergeTrees2(t1, t2)
print()
obj.inOrderTraversal(r)

# 99. Recover Binary Search Tree
# 113. Path Sum II
# 1026. Maximum Difference Between Node and Ancestor