# 101. Symmetric Tree

# Two trees are a mirror reflection of each other if
# 1) Their two roots have the same value
# 2) The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def buildTree(self, nums):

        if not nums: return

        lenNums = len(nums)
        root = TreeNode(nums[0])
        dQ = deque()
        dQ.append(root)

        i = 1
        while i < lenNums:
            node = dQ.popleft()

            if i < lenNums:
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1

            if i < lenNums:
                if nums[i] and node:
                    node.right = TreeNode(nums[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)

    # https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python
    # O(n), O(n) for recursive calls
    def isSymmetric(self, root):
        def isMirror(L, R):
            if not L and not R: return True
            elif not L or not R: return False

            if L.val == R.val:
                outNodes = isMirror(L.left, R.right)
                inNodes = isMirror(L.right, R.left)
                return outNodes and inNodes
            else:
                return False

        if not root: return True
        else: return isMirror(root.left, root.right)

    # O(n), O(n) for que
    def isSymmetric2(self, root):
        if not root: return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            node = stack.pop()
            L = node[0]
            R = node[1]

            if not L and not R: continue
            elif not L or not R: return False
            elif L.val == R.val:
                stack.insert(0, [L.left, R.right])
                stack.insert(0, [L.right, R.left])
            else:
                return False

        return True

nums = [1,2,3,None, None, 5,6]
nums= [1,2,2,3,4,4,3]
obj = Solution()
root = obj.buildTree(nums)
print(obj.isSymmetric2(root))