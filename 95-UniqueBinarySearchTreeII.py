# 95. Unique Binary Search Trees II
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def generateTrees(self, n):

        if n == 0:
            return [[]]
        return self.dfs(1, n + 1)

    def dfs(self, start, end):
        print(f"start={start}, end={end}")
        if start == end:
            return None
        result = []
        for i in range(start, end):
            print(f"i={i}")
            for l in self.dfs(start, i) or [None]:
                print(f" l={l}, start={start}, i={i}, end={end}")
                for r in self.dfs(i + 1, end) or [None]:
                    print(f"  r={r}, i={i}")
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    result.append(node)
        return result

n=2
obj = Solution()
print(obj.generateTrees(n))