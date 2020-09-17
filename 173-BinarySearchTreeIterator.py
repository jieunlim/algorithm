
# 173. Binary Search Tree Iterator
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def binarySearchTree(self, root, node):

        if node.val >= root.val:
            if root.right is None:
                root.right = node
            else:
                self.binarySearchTree(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.binarySearchTree(root.left, node)

    def buildTree(self, alist):

        root = TreeNode(alist[0])

        for i in range(1, len(alist)):
            node = TreeNode(alist[i])
            self.binarySearchTree(root, node)

        self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, root):

        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)


alist = [7,3,15,9,20]
obj = Solution()
root = obj.buildTree(alist)


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.right)
        self.stack.append(root.val)
        self.inOrder(root.left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.stack.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


class BSTIterator1:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        self.allLeftIntoStack(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.stack:return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur = self.stack.pop()
        print(f"[next] cur={cur.val}")
        self.allLeftIntoStack(cur.right)
        return cur.val

    def allLeftIntoStack(self,root):
        while root:
            self.stack.append(root)
            root=root.left

class BSTIterator2:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

print(f"root.val={root.val}")
iterator = BSTIterator(root)
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())