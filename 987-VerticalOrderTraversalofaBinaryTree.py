
# 987. Vertical Order Traversal of a Binary Tree

# O(nlogn)
# O(n)

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
                if arr[i]is not None and node:  #is not None for dealing with '0' value
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


    # k: the number of columns in the results
    # N/K => C,
    # O(ClogC) * O(K)
    # K*N/K*logN/K -> O(NLogN/K)
    def verticalTraversal(self, root):
        from collections import defaultdict

        if not root: return []

        gDict = defaultdict(list)
        gQ = [(root, 0)]

        while gQ:
            newDict = defaultdict(list)
            newQ = []
            for node, col in gQ:
                newDict[col].append((node.val))

                if node.left:
                    newQ.append((node.left, col - 1))
                if node.right:
                    newQ.append((node.right, col + 1))

            for i in newDict:
                gDict[i].extend(sorted(newDict[i]))
                # for n in sorted(newDict[i]):
                #     gDict[i].append(n)
            gQ = newQ

        return [gDict[i] for i in sorted(gDict)]

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        if not root: return None

        gDict = defaultdict(list)
        gQueue = deque([(root, 0)])
        while gQueue:
            localQ = deque()
            localDict = defaultdict(list)
            while gQueue:
                node, col = gQueue.popleft()

                localDict[col].append(node.val)

                if node.left: localQ.append((node.left, col - 1))
                if node.right: localQ.append((node.right, col + 1))

            for k in localDict:
                gDict[k] += sorted(localDict[k])
            gQueue = localQ

        res = []
        for k in sorted(gDict):
            res.append(gDict[k])
        return res

arr = [1,2,3,None,5,None,4]
# arr = [1, None, 2, None, None, 3]
# arr = [3,9,20,None,None,15,7]
# arr=[0,None,1]
# arr=[0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9]
# [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]
obj = Solution()
root = obj.buildTree(arr)
# obj.inOrderT(root)
# print(obj.verticalOrder(root))


# 314. Binary Tree Vertical Order Traversal