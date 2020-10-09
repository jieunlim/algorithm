
# 1612. Check If Two Expression Trees are Equivalent
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
                if arr[i] is not None and node:  # is not None for dealing with '0' value
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

    def checkEquivalence(self, root1, root2):
        def helper(root, arr):
            if root:
                helper(root.left, arr)
                if root.val.isalpha():
                    arr[root.val] += 1
                helper(root.right, arr)

        arr1 = collections.defaultdict(int)
        arr2 = collections.defaultdict(int)
        helper(root1, arr1)
        helper(root2, arr2)
        return arr1 == arr2


root1 = [+,a,+,null,null,b,c]
root2 = [+,+,b,c,a]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
