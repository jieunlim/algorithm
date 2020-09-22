
class Solution:
    # 1245. Tree Diameter
    def treeDiameter(self, edges):
        from collections import defaultdict
        self.diameter = 0
        def helper(node, pre):
            d1 = d2 = 0
            for nei in graph[node]:
                if nei != pre:
                    r = helper(nei, node)
                    if r > d1:
                        d1, d2 = r, d1
                    elif r > d2:
                        d2 = r
            self.diameter = max(self.diameter, d1 + d2)
            return d1 + 1

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        print(f"graph={graph}")
        helper(0, None)
        return self.diameter

obj = Solution()
edges = [[0,1],[0,2]]
edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
print(obj.treeDiameter(edges))

# 1522. Diameter of N-Ary Tree

# 250. Count Univalue Subtrees
# 508. Most Frequent Subtree Sum
# 543. Diameter of Binary Tree
# 1245. Tree Diameter
# 687. Longest Univalue Path
# 124. Binary Tree Maximum Path Sum
# Max Path Sum in a Grid
# 298. Binary Tree Longest Consecutive Sequence
# 549. Binary Tree Longest Consecutive Sequence II