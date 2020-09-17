# 1110. Delete Nodes And Return Forest
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
            print(root.val)
            self.inOrderT(root.left)
            self.inOrderT(root.right)

    def deleteNodeReturnForest(self, root, to_delete):
        to_delete = set(to_delete)
        res = []

        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root

        walk(root, parent_exist=False)
        return res

    # https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/345009/Python-BFS-Solution
    def deleteNodeReturnForest2(self, root, to_delete):
        from collections import deque
        dq = deque([(root, False)])
        res = []

        while dq:
            node, hasParent = dq.popleft()

            if not hasParent and node.val not in to_delete:
                res.append(node)

            hasParent = not node.val in to_delete

            if node.left:
                dq.append((node.left, hasParent))
                if node.left.val in to_delete:
                    node.left = None

            if node.right:
                dq.append((node.right, hasParent))
                if node.right.val in to_delete:
                    node.right = None

        return res


# if delete node - left,right:q append
# if no parent - res.append
# else - leaf node: res.append

arr = [1, 2, 3, 4, 5, 6, 7]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
to_delete = [3, 5]
r = obj.deleteNodeReturnForest2(root, to_delete)

print()
for i in range(len(r)):
    obj.inOrderT(r[i])
    print()
