# 993. Cousins in Binary Tree
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
                if arr[i] and node:
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] and node:
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

    def isCousins(self, root, x, y):
        from collections import deque

        dQ = deque()
        dQ.append((root, 0, None))
        x1 = x2 = -1

        while dQ:
            node, depth, parent = dQ.popleft()

            if node.val == x:
                x1 = depth
                p1 = parent
            elif node.val == y:
                x2 = depth
                p2 = parent

            if x1 > 0 and x2 > 0: break

            if node.left: dQ.append((node.left, depth+1, node))
            if node.right: dQ.append((node.right, depth+1, node))

        return x1 == x2 and p1 != p2


arr = [1,2,3,4]
arr = [1,2,3,None,4]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
print(obj.isCousins(root, 2,3))