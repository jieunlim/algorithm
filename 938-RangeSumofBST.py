# 938. Range Sum of BST

# O(N), N is the number of nodes in the tree
# O(H), H is the height of the tree

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

    # DFS
    def rangeSumofBST(self, root, L, R):

        self.total = 0

        def helper(node):
            if not node: return

            if L <= node.val <= R:
                self.total += node.val

            if node.val > L:
                helper(node.left)
            if node.val < R:
                helper(node.right)

        helper(root)
        return self.total


    def rangeSumofBST2(self, root, L, R):
        if not root:
            return 0

        sum = 0
        if L <= root.val <= R:
            sum += root.val

        if root.val < R:
            sum += self.rangeSumofBST2(root.right, L, R)

        if root.val > L:
            sum += self.rangeSumofBST2(root.left, L, R)

        return sum

obj = Solution()
arr = [5,1,6]
arr = [10,5,15,3,7,None,18]
root = obj.buildTree(arr)
obj.inOrderT(root)

r = obj.rangeSumofBST2(root, 7, 15)
print(f"rtn : {r}")
