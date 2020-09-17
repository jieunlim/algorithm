# 297. Serialize and Deserialize Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize(self, root):
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        return ','.join(res)

    def deserialize2(self, data):
        if not data: return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            print(f"index={index}, nodes[index]={nodes[index]} ")
            print(nodes[index] is not '#')
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

obj = Codec()
data = "'1','2','3,None,None,4,5"
r = obj.deserialize(data)
