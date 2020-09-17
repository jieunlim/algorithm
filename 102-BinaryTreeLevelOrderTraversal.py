# 102. Binary Tree Level Order Traversal

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

    def levelOrder2(self, root):
        if not root: return []

        res, maxV = [], 0
        dic = {}

        myQ = deque()
        myQ.append((root, 0))

        while myQ:
            node, level = myQ.popleft()
            print(f"node.val={node.val}, level={level}")
            if level not in dic:
                dic[level] = [node.val]
            else:
                dic[level].append(node.val)

            if node.left:
                maxV = max(maxV, level+1)
                myQ.append((node.left, level+1))
            if node.right:
                maxV = max(maxV, level+1)
                myQ.append((node.right, level+1))

        print(f"maxV={maxV}")
        for i in range(0, maxV+1):
        # 107. Binary Tree Level Order Traversal II
        # for i in range(maxV, -1, -1):
            res.append(dic[i])
        return res

    def levelOrder22(self, root: TreeNode) -> List[List[int]]:

        from collections import deque, defaultdict

        if not root: return []

        dq = deque([(root, 0)])
        res = []
        resDict = defaultdict(list)
        while dq:
            node, level = dq.popleft()

            resDict[level].append(node.val)

            if node.left: dq.append((node.left, level + 1))
            if node.right: dq.append((node.right, level + 1))

        for key in sorted(resDict):
            res.append(resDict[key])

        return res
    # O(n), O(n)
    def levelOrder(self, root):
        from collections import defaultdict
        if not root: return []
        stack = [(root, 1)]
        maxLevel = 1
        res = []
        dict = defaultdict(list)
        while stack:
            node, level = stack.pop()
            maxLevel = max(maxLevel, level)

            dict[level].append(node.val)

            if node.right: stack.append((node.right, level+1))
            if node.left: stack.append((node.left, level+1))

        for i in range(1, maxLevel+1):
            res.append(dict[i])
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        from collections import defaultdict
        if not root: return []
        resDict = defaultdict(list)
        dq = deque([(root, 0)])
        while dq:
            node, level = dq.popleft()
            resDict[level].append(node.val)

            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))

        res = []
        for k in sorted(resDict):
            res.append(resDict[k])
        return res


alist = [3,9,20,None,None,15,7]
alist=[10, 20]
obj = Solution()
root = obj.buildTree(alist)
print(obj.levelOrder(root))


# 107. Binary Tree Level Order Traversal II
# 103. Binary Tree Zigzag Level Order Traversal