# 1490. Clone N-ary Tree
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return None

        node = Node(root.val, [])

        for i in range(len(root.children)):
            node.children.append(self.cloneTree(root.children[i]))

        return node

