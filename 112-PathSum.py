
# 112. Path Sum
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

    # recursion
    # O(N), N is the number of nodes
    # space O(N), in the worst case, the tree is completely unbalanced,
    # the recursion call would occur N times(the height of the tree)
    # but, in the best case, O(logN)
    def hasPathSum(self, root, sum):
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def pathSum(self, root, sum):
        def helper(node, target):
            if not node:
                return False

            target = target - node.val

            if target == 0 and not node.left and not node.right:
                return True

            return helper(node.left, target) or helper(node.right, target)

        return helper(root, sum)

    # iteration
    # DFS, stack
    def hasPathSum2(self, root, sum):

        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

# nums = [1,2,3,None, None, 5,6]
nums= [1,2,2,3,4,4,3]
nums=[1,2,3]
sum = 3
obj = Solution()
root = obj.buildTree(nums)
print(obj.hasPathSum2(root, sum))