
# 113. Path Sum II
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.val = data
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

        self.preOrderTraversal(root)
        return root

    def preOrderTraversal(self, node):
        if node:
            print(node.val)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def pathSum(self, root, sum):

        def findSum(node, target, path):
            if not node:
                return

            target -= node.val
            path = path+[node.val]
            # path += [node.val]  #this doesn't work - same path variable reference
            if not node.left and not node.right and target == 0:
                res.append(path)

            findSum(node.left, target, path )
            findSum(node.right, target, path)

        if not root:
            return []
        res = []
        findSum(root, sum, [])
        return res

    def pathSum2(self, root, sum):
        def helper(node, target, path):

            if not node:
                return

            t = target - node.val
            # print(f"node={node.val}, t={t}")
            if t == 0 and not node.left and not node.right:
                res.append(path)

            if node.left: helper(node.left, t, path + [node.left.val])
            if node.right: helper(node.right, t, path + [node.right.val])

        if not root:
            return []
        res = []
        helper(root, sum, [root.val])
        return res

    def pathSum3(self, root, sum):

        if not root: return False
        stack = [(root, sum-root.val, [root.val])]
        path = []
        res = []
        while stack:
            node, target, path = stack.pop()

            if target == 0 and not node.left and not node.right:
                res.append(path)

            if node.left: stack.append((node.left, target-node.left.val, path+[node.left.val]))
            if node.right: stack.append((node.right, target-node.right.val, path+[node.right.val]))

        return res


# nums = [1,2,3,None, None, 5,6]
nums= [1,2,2,3,4,4,3]
nums=[1,2,3]
sum = 3
nums=[5,4,8,11,None,13,4,7,2,None, None,None, None,5,1]
sum=22
obj = Solution()
root = obj.buildTree(nums)
print(obj.pathSum(root, sum))


'''
# path += [node.val]  #this doesn't work - same path variable reference
a = [1,2]
print(id(a))
a += [1]
print(id(a))
b = [1,2]
print(id(b))
b =b+[1]
print(id(b))
print(a)
'''