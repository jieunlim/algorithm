# 1214. Two Sum BSTs
# Given two binary search trees,
# return True if and only if there is a node in the first tree
# and a node in the second tree whose values sum up to a given integer target.

from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, alist):

        if not alist:
            return

        root = TreeNode (alist[0])
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

        # self.inOrderTraversal(root)
        return root

    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)


    # https://leetcode.com/problems/two-sum-bsts/discuss/397624/Simple-Stack-Solution
    # stack, inorder traversal/ reverse inorder traversal - like two pointers of sorted array
    # root1 from smallest value to the largest, root2 from largest to smallest
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        stack1, stack2 = [], []
        while True:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.right
            if not stack1 or not stack2: break
            if stack1[-1].val + stack2[-1].val == target:
                return True
            elif stack1[-1].val + stack2[-1].val < target:
                root1 = stack1.pop().right
            else:
                root2 = stack2.pop().left
        return False

    def twoSumBSTs2(root1, root2, target):
        dq = deque([root1])
        r1 = set() #fast enough if use set instead of array

        while dq:
            node = dq.popleft()
            r1.add(node.val)

            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)

        dq = deque([root2])
        while dq:
            node = dq.popleft()

            if target - node.val in r1:
                return True

            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)

        return False

    def twoSumBSTs3(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        stack1, stack2 = [], []
        while True:
            # LeftMost Node
            while root1:
                print(f"root1: {root1.val}")
                stack1.append(root1)
                root1 = root1.left
            # RighMost Node
            while root2:
                print(f"root2: {root2.val}")
                stack2.append(root2)
                root2 = root2.right

            # If either is empty then break.
            if not stack1 or not stack2: break

            print(f"stack1[-1].val={stack1[-1].val} + stack2[-1].val={stack2[-1].val}")
            if stack1[-1].val + stack2[-1].val == target:
                return True
            # move to next possible node in the inorder traversal of root 1
            elif stack1[-1].val + stack2[-1].val < target:
                root1 = stack1.pop().right
                if root1: print(f"root1.val: {root1.val}")
            # move to next possible node in the reverse inorder traversal of root 2
            else:
                if root2: print(f"root2: {root2.val}, stack2={stack2}")
                root2 = stack2.pop().left
                if root2: print(f"root2: {root2.val}, stack2={stack2}")

        return False

    def twoSumBSTs22(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        hashtree1 = set()

        stack = [root1]
        while stack:
            node = stack.pop()
            hashtree1.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        stack = [root2]
        while stack:
            node = stack.pop()
            if (target - node.val) in hashtree1:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False

    def twoSumBSTs1(self, root1, root2, target):
        # by ms, accepted but too late, 8696 ms
        def twoSumBSTs_re(root1, root2):

            if not root1 or not root2:
                return

            dq = deque()
            dq.append(root2)

            while len(dq) > 0:
                node = deque.popleft(dq)
                print(f"root2_nodes={root2_nodes}")

                root2_nodes.add(node.val)
                s = target - root1.val
                print(f"root1.val={root1.val}, s={s}")

                if s in root2_nodes:
                    return True
                else:
                    if node.left:
                        dq.append(node.left)

                    if node.right:
                        dq.append(node.right)


            return twoSumBSTs_re(root1.left, root2) or twoSumBSTs_re(root1.right, root2)

        root2_nodes = set()
        rtn = twoSumBSTs_re(root1, root2)
        return False if rtn is None else True


alist1 = [6,2,8,1,3,7,9]
alist2 = [5,3,10,1,4,6,12]
target=10

alist1 = [7,2,8]
alist2=[5,4,6]
target = 11

# alist1=[-610851256,-653710341,370681985,-684322521,None,-99709414,945937000,-723663811,None,-580534514,175879876,684879230,961162608,-937470592,None,None,-300171034,26171351,216952004,586959211,722844782,953939489,989534661,None,-766632327,-375831089,-216679007,-10713080,103126520,None,343409064,540698705,660693010,None,894076654,None,None,None,None,-813292023,None,-496932482,-304607959,-228730335,-126869030,-78270931,22440306,84915568,None,307851156,None,434200343,None,None,None,846779650,None,-826002807,None,None,-483519915,-334445856,None,None,None,-135095123,None,None,None,None,None,83812730,None,None,None,None,None,836900978,None,-893449855,-819573989,None,-442688630,None,None,None,None,40242181,None,None,None,-901146738]
# alist2=[-789314604,-844978429,-362754072,-884801305,-842381632,-478151046,61096204,None,None,None,None,-745017955,-445455117,-206589393,512329594,None,-740359122,-466990471,-420769635,-317219442,-108708327,388674482,844021027,None,-533290204,None,None,-422661229,None,None,-209171221,-112908812,None,296061830,484713586,674571946,994804552,-692388982,None,None,None,None,None,None,None,188484963,386640458,399688904,None,583260301,808930864,962289719,None,None,-619367458,None,None,None,None,None,None,524969019,589842534,739755144,None,954377409,None,None,None,None,540622433,None,None,None,748416803,939513678,None,None,568310964]
# target=68839864

# alist1 = [0,-10,10]
# alist2 = [5,1,7,0,2]
# target = 18
obj = Solution()
r1 = obj.buildTree(alist1)
r2 = obj.buildTree(alist2)
# print(obj.twoSumBSTs2(r1,r2, target))
print(obj.twoSumBSTs(r1,r2, target))