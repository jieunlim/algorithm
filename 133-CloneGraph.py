# 133. Clone Graph
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):

        def helper(node):
            if node in visited:
                return visited[node]
            newNode = Node(node.val, [])
            visited[node] = newNode

            # if node.neighbors:
            for nei in node.neighbors:
                newNode.neighbors.append(helper(nei))

            return newNode

        if not node: return None
        visited = {}
        return helper(node)

adjList = [[2,4],[1,3],[2,4],[1,3]]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

obj = Solution()
rtn = obj.cloneGraph(node1)
print(rtn.val, id(rtn), id(node1))
for nei in rtn.neighbors:
    print(nei.val)









class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = None
from collections import deque
class Solution(object):

    def cloneGraph2(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node):

        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

    def cloneGraph3(self, node):

        def cloneG(node):
            if not node: return None

            if node in visited:
                return visited[node]

            cloneNode = Node(node.val, [])
            visited[node] = cloneNode

            if node.neighbors:
                for nei in node.neighbors:
                    cloneNode.neighbors.append(cloneG(nei))

            return cloneNode

        visited = {}
        return cloneG(node)



# 138. Copy List with Random Pointer
# 1485. Clone Binary Tree With Random Pointer