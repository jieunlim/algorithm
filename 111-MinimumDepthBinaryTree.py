# 111. Minimum Depth of Binary Tree
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # DFS-Recursion O(N), O(N)
    def minDepth_DFS_Re(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        print(f"root.data={root.data}")
        left_depth = float('inf')
        right_depth = float('inf')

        if root.left is not None:
            left_depth = self.minDepth_DFS_Re(root.left)

        if root.right is not None:
            right_depth = self.minDepth_DFS_Re(root.right)

        print(f"  root.data={root.data} left_depth={left_depth}, right_depth={right_depth}")

        return 1 + min(left_depth, right_depth)

    # DFS-stack O(N), O(N)
    def minDepth_dfs(self, root):

        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')
            print(f"stack={stack}, min_depth={min_depth}")

        while stack:
            depth, root = stack.pop()
            print(f"depth={depth}, root={root.data}")

            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)

            for c in children:
                if c:
                    stack.append((depth + 1, c))
                    print(f"   [for-if] c={c.data}, stack={stack}")
            print(f"min_depth={min_depth}")
        return min_depth

    # BFS-queue O(N), O(N)
    def minDepth_bfs(self, root):
        from collections import deque

        if not root:
            return 0
        else:
            node_deque = deque([(1, root), ])

        while node_deque:
            depth, root = node_deque.popleft()
            print(f"depth={depth}, root={root.data}")
            children = [root.left, root.right]
            if not any(children):
                print(f" root={root.data}, return :", depth)
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))

    def buildTree(self, alist):

        from collections import deque

        if not alist:
            return

        root = TreeNode(alist[0])
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
            print(node.data)
            self.inOrderTraversal(node.right)


arr = [3, 9, 20, None, None, 15, 7]
# arr = [3, 9, 20, 10, 4]
# arr = [1, 2]  # 2
obj = Solution()
root = obj.buildTree(arr)

# print("minDepth:", obj.minDepth(root))
# print("minDepth:", obj.minDepth_DFS_Re(root))
print("minDepth:", obj.minDepth_dfs(root))
# print("minDepth:", obj.minDepth_bfs(root))