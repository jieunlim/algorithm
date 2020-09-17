
# 653. Two Sum IV - Input is a BST
# Hashset with DFS (recursion, stack) or BFS(Queue)
# O(n), O(n)
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

    # DFS
    def findTarget(self, root, k):

        def findT(node):
            if not node:
                return False

            print(f"node ={node.data}")
            s = k - node.data

            if s in nodes:
                return True

            nodes.add(node.data)

            return findT(node.left) or findT(node.right)

        nodes = set()
        return findT(root)

    # DFS
    def findTarget2(self, root, k):
        values = []
        roots = [root]
        while (len(roots)):
            node = roots.pop(0)
            if k - node.data in values: return True
            values.append(node.data)
            if node.left != None: roots.append(node.left)
            if node.right != None: roots.append(node.right)

        return False

    # BFS
    def findTarget3(self, root, k):
        if not root:
            return False
        queue, seen = deque([root]), set()
        while queue:
            cur = queue.popleft()
            if k - cur.data in seen:
                return True
            else:
                seen.add(cur.data)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return False

alist = [5,3,6,2,4,None,7]
k = 9
obj = Solution()
r = obj.buildTree(alist)
print(obj.findTarget(r, k))