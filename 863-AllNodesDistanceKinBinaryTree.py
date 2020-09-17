# 863. All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/360110/Python-Basically-Let's-build-a-graph.
# time O(N)
# space O(N)


from collections import deque, defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, arr):
        if not arr: return

        root = TreeNode(arr[0])

        dQ = deque()
        dQ.append(root)

        i = 1
        while dQ:
            node = dQ.popleft()

            if i < len(arr):
                if arr[i]is not None and node:  #is not None for dealing with '0' value
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] is not None and node:
                    node.right = TreeNode(arr[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        # self.inOrderT(root)
        return root

    def inOrderT(self, root):
        if root:
            self.inOrderT(root.left)
            print(root.val)
            self.inOrderT(root.right)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        from collections import deque, defaultdict
        if not root: return []

        graph = defaultdict(list)
        self.buildGraph(graph, None, root)

        visited = set()
        res = []
        dq = deque([(target, 0)])
        while dq:

            node, distance = dq.popleft()

            visited.add(node)

            if distance == K:
                res.append(node.val)
            elif distance < K:
                for g in graph[node]:
                    if g not in visited:
                        dq.append((g, distance + 1))
        return res

    def buildGraph(self, graph, parent, child):

        if parent and child:
            graph[parent].append(child)
            graph[child].append(parent)

        if child.left: self.buildGraph(graph, child, child.left)
        if child.right: self.buildGraph(graph, child, child.right)

    ''' 
    def distanceK(self, root, target, K):
        graph = defaultdict(list)
        self.buildGraph(None, root, graph)
        print(graph)
        res = []
        visited = set()
        dQ = deque([(target.val, 0)])
        while dQ:
            node, distance = dQ.popleft()

            if node in visited: continue
            visited.add(node)

            if distance == K:
                res.append(node)
            elif distance < K:
                for c in graph[node]:
                    dQ.append((c, distance + 1))
        return res

    def buildGraph(self, parent, child, graph):

        if parent and child:
            graph[parent.val].append(child.val)
            graph[child.val].append(parent.val)

        if child.left: self.buildGraph(child, child.left, graph)
        if child.right: self.buildGraph(child, child.right, graph)

    '''

arr = [3,5,1,6,2,0,8,None, None,7,4]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
target = 5
K = 2
print(obj.distanceK(root, root.left, K))












#########################################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def buildTree(self, nums):
        root = TreeNode(nums[0])
        dq = deque()
        dq.append(root)

        i = 1
        while dq:
            node = dq.popleft()

            if i < len(nums):
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    dq.append(node.left)
                else:
                    dq.append(None)
            i+=1
            if i < len(nums):
                if nums[i] and node:
                    node.right = TreeNode(nums[i])
                    dq.append(node.right)
                else:
                    dq.append(None)
            i+=1
        self.traversal(root)
        return root

    def traversal(self, root):
        if root:
            self.traversal(root.left)
            print(root.val)
            self.traversal(root.right)

    # Graph, Queue
    # Graph- Adjacent list - node:neighbors
    def buildGraph(self, node, parent, graph):
        if node is None:
            return


        if parent is not None:
            graph[node].append(parent)
            # print(f"node={node.val}, parent={parent.val}")

        if node.left is not None:
            graph[node].append(node.left)
            # print(f"node={node.val}, node.left={node.left.val}")
            self.buildGraph(node.left, node, graph)

        if node.right is not None:
            graph[node].append(node.right)
            # print(f"node={node.val}, node.right={node.right.val}")
            self.buildGraph(node.right, node, graph)

    def distanceK2(self, root, target, K):

        from collections import defaultdict
        # vetex: [parent, left, right]
        graph = defaultdict(list)

        # DFS to build graph
        self.buildGraph(root, None, graph)

        # BFS to retrieve the nodes with given distance
        # Starting from the target node
        q = [(target, 0)]

        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []
        while q:
            node, distance = q.pop(0)
            if node in visited:
                continue
            visited.add(node)

            # we've reached the desired distance/radius
            if K == distance:
                ans.append(node.val)

            # we haven't reached the desired distance, keep going
            elif distance < K:
                for child in graph[node]:
                    q.append((child, distance + 1))
            # exceed the desired distance
            # No need to go further

        return ans

    # Map, Recursion DFS
    # maps: node-parent
    def buildParentMap(self, node, parent, parentMap):
        if node is None:
            return
        parentMap[node] = parent
        self.buildParentMap(node.left, node, parentMap)
        self.buildParentMap(node.right, node, parentMap)

    def distanceK(self, root, target, K):

        # node: parent
        parentMap = {}

        # DFS to build the map that maps a node to its parent.
        self.buildParentMap(root, None, parentMap)

        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []

        # Again, DFS to retrieve the nodes within the given distance
        #  this time with the help of the parentMap.
        # Starting from the target node
        def dfs(node, distance):
            if node is None or node in visited:
                return

            visited.add(node)

            if distance == K:
                ans.append(node.val)
            elif distance < K:
                dfs(node.left, distance + 1)
                dfs(node.right, distance + 1)
                dfs(parentMap[node], distance + 1)
            # else exceed the scope, no need to explore further

        dfs(target, 0)

        return ans


nums = [3,5,1,6,2,0,8,None,None,7,4]
target=5
K=2
obj = Solution()
r = obj.buildTree(nums)
print()
print(obj.distanceK2(r, r.left, K))
