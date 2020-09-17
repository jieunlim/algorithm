# 270. Closest Binary Search Tree Value
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def binarySearchTree(self, root, node):

        if node.val >= root.val:
            if root.right is None:
                root.right = node
            else:
                self.binarySearchTree(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.binarySearchTree(root.left, node)

    def buildTree(self, alist):

        root = TreeNode(alist[0])

        for i in range(1, len(alist)):
             node = TreeNode(alist[i])
             self.binarySearchTree(root, node)

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, root):

        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)

    # def closestValue(self, root, target):
    #     a = root.val
    #     kid = root.left if target < a else root.right
    #     if not kid: return a
    #     b = self.closestValue(kid, target)
    #     return min((b, a), key=lambda x: abs(target - x))
    #
    # def closestValue2(self, root, target):
    #     path = []
    #     while root:
    #         path += root.val,
    #         root = root.left if target < root.val else root.right
    #     return min(path[::-1], key=lambda x: abs(target - x))

    def closestValue(self, root, target):
        self.closest = float('inf')

        def helper(root):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val

            # Target should be located on left subtree
            if target < root.val and root.left:
                helper(root.left)

            # target should be located on right subtree
            if target > root.val and root.right:
                helper(root.right)

        helper(root)
        return self.closest

    def closestValue2(self, root, target):
        dq = deque([root])
        minVal = float('inf')

        while dq:
            node = dq.popleft()

            if  abs(node.val-target) < abs(minVal - target):
                minVal = node.val

            print(node.val)
            if node.val > target and node.left: dq.append(node.left)
            if node.val < target and node.right: dq.append(node.right)

        return minVal

    def closestValue3(self, root, target):
        if not root: return

        closest = [root.val, abs(root.val - target)]
        dq = deque([(root)])

        while dq:
            node = dq.popleft()

            if abs(node.val - target) < closest[1]:
                closest[0] = node.val
                closest[1] = abs(node.val - target)

            if node.val > target and node.left: dq.append(node.left)
            if node.val < target and node.right: dq.append(node.right)

        return closest[0]

alist = [4,2,5,1,3]
obj = Solution()
root = obj.buildTree(alist)
target = 3.714286
print()
print(obj.closestValue(root, target))