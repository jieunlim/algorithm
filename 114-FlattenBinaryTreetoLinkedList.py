# 114. Flatten Binary Tree to Linked List

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


    def flatten(self, root: TreeNode) -> None:
        def flattenTree(self, node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            # Recursively flatten the left subtree
            leftTail = flattenTree(node.left)

            # Recursively flatten the right subtree
            rightTail = flattenTree(node.right)

            # If there was a left subtree, we shuffle the connections
            # around so that there is nothing on the left side
            # anymore.
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            # We need to return the "rightmost" node after we are
            # done wiring the new connections.
            return rightTail if rightTail else leftTail

        flattenTree(root)

    def flatten2(self, root: TreeNode) -> None:
        if not root: return None

        node = root
        while node:
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right

    def flatten3(self, root):

        def helper(node):
            nonlocal prev

            if not node: return
            helper(node.right)
            helper(node.left)
            node.right = prev
            node.left = None
            prev = node

        prev = None
        helper(root)


obj = Solution()
arr = [6, 2, 9]
root = obj.buildTree(arr)
obj.inOrderT(root)
print()

obj.flatten3(root)
obj.inOrderT(root)