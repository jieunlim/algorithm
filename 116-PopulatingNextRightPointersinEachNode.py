# 116. Populating Next Right Pointers in Each Node
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def buildTree(self, arr):

        if not arr:
            return

        root = TreeNode(arr[0])
        myQ = deque()
        myQ.append(root)
        i = 1
        while myQ:
            node = myQ.popleft()

            if i < len(arr):
                if arr[i] and node:
                    node.left = TreeNode(arr[i])
                    myQ.append(node.left)
                else:
                    myQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] and node:
                    node.right = TreeNode(arr[i])
                    myQ.append(node.right)
                else:
                    myQ.append(None)
            i += 1

        # self.inOrder(root)
        # print(f"---")
        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val, root.next.val) if root.next else print(root.val, "None")
            self.inOrder(root.right)

    # BFS
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root

    # BFS - using Q size
    def connect2(self, root: 'Node') -> 'Node':
        import collections

        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])

        # Outer while loop which iterates over
        # each level
        while Q:

            # Note the size of the queue
            size = len(Q)

            # Iterate over all the nodes on the current level
            for i in range(size):

                # Pop a node from the front of the queue
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
        return root

    # recursion
    def connect2(self, root ) :
        if not root:
            return None

        if root.right: #perfect binary tree
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

    # DFS
    def connect3(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                stack.append(curr.right)
                stack.append(curr.left)
        return root

root = [1,2,3,4,5,6,7]
obj = Solution()
root = obj.buildTree(root)
obj.inOrder(obj.connect2(root))

# 545. Boundary of Binary Tree
# 199. Binary Tree Right Side View