
# 337. House Robber III
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:

    # def rob2(self, root):
    #     def dfs(node):
    #         if not node: return 0, 0
    #         l, r = dfs(node.left), dfs(node.right)
    #
    #         print(f"max(l){max(l)} + max(r){max(r)}")
    #         print(f"node.val {node.val} + l[0] {l[0]} + r[0] {r[0]}")
    #         return max(l) + max(r), node.val + l[0] + r[0]
    #     return max(dfs(root))

    def rob(self, root):

        myQ = deque()
        myQ.append((root, 0))

        oddSum = evenSum = 0

        while len(myQ) > 0:
            node, i = myQ.popleft()

            if i%2 == 0:
                evenSum += node.val
            else:
                oddSum += node.val

            if node.left:
                myQ.append((node.left, i+1))
            if node.right:
                myQ.append((node.right, i+1))

        return max(evenSum, oddSum)


    def buildTree(self, alist):

        if not nums:
            return

        root = TreeNode (nums[0])
        myQ = deque()
        myQ.append(root)

        i = 1
        while len(myQ) > 0:
            node = myQ.popleft()

            if i < len(nums):
                if nums[i] is not None and node:
                    node.left = TreeNode(nums[i])
                    myQ.append(node.left)
                else:
                    myQ.append(None)

            i += 1

            if i < len(nums):
                if nums[i] is not None and node:
                    node.right = TreeNode(nums[i])
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


# nums=[3,2,3,None,3,None,1]
# nums=[3,4,5,1,3,None,1]
nums=[1,2,3,4,5,6,7,8,9,10,None, 11,None,12]
obj = Solution()
root = obj.buildTree(nums)
print("return:", obj.rob(root))