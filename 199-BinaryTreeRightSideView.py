# 199. Binary Tree Right Side View

# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56248/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, nums):
        from collections import deque

        if not arr: return
        root = TreeNode(nums[0])

        myQ = deque()
        myQ.append(root)

        i = 1
        while myQ:
            node = myQ.popleft()

            if i < len(nums):
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    myQ.append(node.left)
                else:
                    myQ.append(None)
            i += 1

            if i < len(nums):
                if nums[i] and node:
                    node.right = TreeNode(nums[i])
                    myQ.append(node.right)
                else:
                    myQ.append(None)
            i += 1
        # self.inOrder(root)
        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

    # DFS recursively
    # O(N)
    # O(H) - recursion stack
    def rightSideView11(self, root):
        def helper(level, node):
            if len(res) == level:
                res.append(node.val)

            if node.right:
                helper(level + 1, node.right)
            if node.left:
                helper(level + 1, node.left)

        if not root: return []
        res = []
        helper(0, root)
        return res

    # def rightSideView1(self, root):
    #     res = []
    #     self.dfs(root, 0, res)
    #     return res
    #
    # def dfs(self, root, level, res):
    #     if root:
    #         if len(res) == level:
    #             res.append(root.val)
    #         print(f"root={root.val}, res={res}, level={level}")
    #         self.dfs(root.right, level + 1, res)
    #         self.dfs(root.left, level + 1, res)

    # DFS + stack
    def rightSideView2(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                print(f"curr.val={curr.val}, len(res)={len(res)}, level={level}")
                if len(res) == level:
                    res.append(curr.val)
                    print(f"res={res}")
                stack.append((curr.left, level + 1))
                stack.append((curr.right, level + 1))
        return res

    # BFS + queue
    # O(N)
    # O(D) - D is a tree diameter
    def rightSideView3(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                queue.append((curr.right, level + 1))
                queue.append((curr.left, level + 1))
        return res


arr = [1,2,3,None,4,None,5]
arr = [1,2,3,4,None, None, 5, 6]
obj = Solution()
root = obj.buildTree(arr)
print(obj.rightSideView3(root))

# 545. Boundary of Binary Tree
# 116. Populating Next Right Pointers in Each Node


'''
 
    def rightSideView(self, root):
        if not root: return []
        dq = deque()
        dq.append((root, 0))
        res = []

        while dq:
            node, level = dq.popleft()

            if len(res) == level:
                res.append(node.val)

            if node.right: dq.append((node.right, level+1))
            if node.left: dq.append((node.left, level+1))

        return res

    def rightSideView2(self, root):

        def helper(node, level):

            if not node:
                return

            if len(res) == level:
                res.append(node.val)

            if node.right: helper(node.right, level+1)
            if node.left: helper(node.left, level+1)

        if not root: return []
        res = []
        helper(root, 0)
        return res

'''