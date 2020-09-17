
# 545. Boundary of Binary Tree

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

    def boundaryOfBinaryTree2(self, root):

        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)

                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left, isleft, isright)
                    dfs(root.right, isleft, isright)

                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    boundary.append(root.val)

        # The main idea is to carry the flag isleft and isight
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        if not root: return []
        boundary = [root.val]

        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary

    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                print(f"dfs_leftmost-return")
                return
            boundary.append(node.val)
            print(f"boundary={boundary}")
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                print(f"dfs_leaves-return")
                return
            print(f"dfs_leaves-{node.val}")
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
                print(f"boundary={boundary}")
            dfs_leaves(node.right)

        # def dfs_leaves(node):
        #     if not node:
        #         return
        #     if node != root and (not node.left and not node.right):
        #         self.boundary.append(node.val)
        #     else:
        #         dfs_leaves(node.left)
        #         dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                print(f"dfs_rightmost-return")
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary


arr = [1,None, 2, None, None, 3,4]
# arr = [1,2,3,4,5,6,None,None, None, 7,8,9,10]
obj = Solution()
root = obj.buildTree(arr)
print(obj.boundaryOfBinaryTree(root))


# 116. Populating Next Right Pointers in Each Node
# 199. Binary Tree Right Side View