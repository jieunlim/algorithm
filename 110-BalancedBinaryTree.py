# 110. Balanced Binary Tree
# Compute the tree's height via recursion
# solution 2
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, alist):
        if len(alist) < 1:
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


    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.data)
            self.inOrderTraversal(root.right)


    # DFS
    # time O(N), space O(N)
    def isBalanced_1(self, root):
        def check(node):
            if not node:
                return True

            L = check(node.left)
            if L == False: return False
            R = check(node.right)
            if R == False: return False

            if abs(L - R) > 1: return False
            return max(L, R) + 1

        return check(root) != False


    def isBalanced_2(self, root):
        def check(node):
            if not node:
                return 0

            L = check(node.left)
            if L == -1: return -1
            R = check(node.right)
            if R == -1: return -1

            if abs(L - R) > 1: return -1
            return max(L, R) + 1

        return check(root) != -1

alist = [3, 9, 20, None, None, 15, 7]  # True
obj = Solution()
r = obj.buildTree(alist)
print("balanced:", obj.isBalanced_1(r))

class Solution2:
###Solution 1 copied
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1

        print(f"height - root.left={id(root.left)}, root.val={root.data}, root.right={id(root.right)}")

        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced2(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        print(f"root.val={root.data}, root.left = {id(root.left)}, root.right = {id(root.right)}")

        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

######

#Solution 1 - copy and edited by ms
# time O(NlgN), space O(N)

    def isBalanced1(self, root):
        def getHeight(root):
            if not root:
                return -1
            # print(f"[getHeight]root.data={root.data}, left={id(root.left)}, right={id(root.right)}")
            print(f"[getHeight]root.data={root.data}")
            return 1 + max(getHeight(root.left), getHeight(root.right))

        def check(root):
            if not root:
                return True

            # print(f"root.data={root.data}, left={id(root.left)}, right={id(root.right)}")
            print(f"root.data={root.data}")
            if abs(getHeight(root.left) - getHeight(root.right)) > 1:
                return False

            left = check(root.left)
            print(f"root.data={root.data}, left=", left)
            if left == False:
                return False
            right = check(root.right)
            print(f"root.data={root.data}, right=", right)
            if right == False:
                return False

            # return max(left, right) + 1
            return True
        return check(root) != False

# Solution 2
# This is a good solution - O(n) O(n)

    # def isBalanced2(self, root):
    #     def check(root):
    #         if not root:
    #             return 0
    #
    #         left = check(root.left)
    #         if left == -1:
    #             return -1
    #         right = check(root.right)
    #         if right == -1:
    #             return -1
    #
    #         if abs(left - right) > 1:
    #             return -1
    #         return max(left, right) + 1
    #
    #     return check(root) != -1

    def isBalanced2(self, root):
        def check(root):
            if not root:
                return True

            print("root.data=",root.data)
            left = check(root.left)
            if left == False:
                return False
            right = check(root.right)
            if right == False:
                return False

            print(f"root.data={root.data}, left={left}, right={right}, difference={abs(left-right)}")
            if abs(left - right) > 1:
                return False

            return max(left, right) + 1

        return check(root) != False

#######

# alist = [1,2,2,3,3,None,None,4,4]
# alist = [50,30,None,10,80,None, None,3,4] #False
# alist=[]
alist=[3,9,20,None,None,15,7] #True
obj = Solution2()

r = obj.buildTree(alist)
# print("balanced:", obj.isBalanced1(r))
# print("balanced:", obj.isBalanced1(r))


'''
110. Balanced Binary Tree
<Solution1>
def isBalanced1(self, root):
  def getHeight(root):
    if not root:
      return -1
    # print(f"[getHeight]root.data={root.data}, left={id(root.left)}, right={id(root.right)}")
    return 1 + max(getHeight(root.left), getHeight(root.right))
  def check(root):
    if not root:
      return True
    # print(f"root.data={root.data}, left={id(root.left)}, right={id(root.right)}")
    if abs(getHeight(root.left) - getHeight(root.right)) > 1:
      return False
    left = check(root.left)
    if left == False:
      return False
    right = check(root.right)
    if right == False:
      return False
    return True
  return check(root) != False
예) [3,9,20,None,None,15,7] 트리가 있다고 하고,
3 이 root, 9가 왼쪽, 20 이 오른쪽, 20 아래에 15, 7이 있는 트리입니다.
Solution1은 root node 3의 height를 먼저 계산하기 위해 트리 전체를 순회시작합니다.
처음으로 root.left인 9의 height 를 구하고, 9는 양쪽에 none이므로 양쪽 모두 -1을 리턴하고 max값은 -1이므로 9의 height는 0 이 됩니다.
다음 root.right인 20으로 가서 height를 구하는데, 20의 left 가 있으므로…내려가기 시작, 15 와 7의 height를 다 구한 후 20의 height를 구하고
9와 20의 height를 이용해서 root인 3의 height값 2를 얻게 됩니다.
여기까지가 abs(getHeight(root.left) - getHeight(root.right)) 이거 한 줄 수행한 상태이고, root 노드 하나에 대해서 balanced를 구하기 위해서 이미 트리 전체를 한번 순회하였습니다. balanced가 아니면 여기서 false를 리턴하고 로직은 끝.
루트 아래 노드들의 balance를 구하기 시작, 이것이 check(root.left)입니다. 9의 balance를 구하고 balanced가 아니면 false리턴하고 여기서 로직은 끝, balanced라면
root.right인 20으로 가서 같은 과정을 반복하며 balance를 구합니다.
root.data=3
[getHeight]root.data=9
[getHeight]root.data=20
[getHeight]root.data=15
[getHeight]root.data=7
root.data=9
root.data=20
[getHeight]root.data=15
[getHeight]root.data=7
root.data=15
root.data=7
balanced: True
<Solution 2>
def isBalanced2(self, root):
  def check(root):
    if not root:
      return True
    #print("root.data=",root.data)
    left = check(root.left)
    if left == False:
      return False
    right = check(root.right)
    if right == False:
      return False
    #print(f"root.data={root.data}, left={left}, right={right}, difference={abs(left-right)}")
    if abs(left - right) > 1:
      return False
    return max(left, right) + 1
  return check(root) != False
Solution2는 check(root.left)를 먼저 부르기 때문에 root인 3을 호출 후, 3은 다시 left인 9를 호출, 9의 balanced가 False라면 여기서 return false., 
balanced라면 right인 20으로 가서 
20의 left인 15와 7의 balance를 구하고 false가 아니면 
이 값을 이용해서 20의 balance를 구합니다. false가 아니면
9와 20의 balance를 비교해서 root인 3의 balance를 구하는 것입니다.
root.data= 3
root.data= 9
root.data=9, left=True, right=True, difference=0
root.data= 20
root.data= 15
root.data=15, left=True, right=True, difference=0
root.data= 7
root.data=7, left=True, right=True, difference=0
root.data=20, left=2, right=2, difference=0
root.data=3, left=2, right=3, difference=1
balanced: True
Solution1은 각 루트노드의 balance를 구하기 위해 매번 트리 절반씩 줄어들면서 순회하는데, 각 root노드마다 이 과정을 수행하므로 time complexity가 O(NlgN),
Solution2는 맨 아래 노드부터 올라오면서 한번만 순회를 하기 때문에 O(N) 입니다.
둘 다 recursion을 사용하기 때문에 메모리 stack에 대한 공간 비용으로 space complexity는 O(N) 입니다
'''