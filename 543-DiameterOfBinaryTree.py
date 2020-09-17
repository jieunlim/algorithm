# 543. Diameter of Binary Tree

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
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
            print(node.data)
            self.inOrderTraversal(node.right)

    # DFS, O(N), O(H)
    def diameterOfBinaryTree1(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return 0

            L = dfs(node.left)
            R = dfs(node.right )

            self.ans = max(self.ans, L+R)
            print(f"L={L}, R={R}, self.ans={self.ans}")
            return max(L, R) + 1

        dfs(root)
        return self.ans

    def diameterOfBinaryTree(self, root):
        self.maxVal = 0
        def helper(root):
            if not root:
                return -1

            L = helper(root.left) + 1
            R = helper(root.right) + 1

            self.maxVal = max(L + R, self.maxVal)

            return max(L, R)

        helper(root)
        return self.maxVal

alist = [1,2,3,4,5,6,7,8,9]

obj = Solution()
r = obj.buildTree(alist)
print(f"ans: {obj.diameterOfBinaryTree1(r)}")
