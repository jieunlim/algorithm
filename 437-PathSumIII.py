# 437. Path Sum III

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def buildTree(self, nums):

        if not nums: return
        lenNum = len(nums)

        root = TreeNode(nums[0])
        dQ = deque()
        dQ.append(root)

        i = 1
        while len(dQ) > 0:

            node = dQ.popleft()

            if i < lenNum:
                if nums[i] and node:
                    node.left = TreeNode(nums[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < lenNum:
                if nums[i] and node:
                    node.right = TreeNode(nums[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        self.inOrderTraversal(root)
        return root
    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.val)
            self.inOrderTraversal(root.right)


    # 52ms
    # O(N), space O(N)
    def pathSum(self, root, sum):
        from collections import defaultdict

        def helper(node, sumSofar=0):
            if not node:
                return 0
            sumSofar += node.val
            numOfSum = dict[sumSofar - sum]
            dict[sumSofar] += 1
            res = numOfSum + helper(node.left, sumSofar) + helper(node.right, sumSofar)
            dict[sumSofar] -= 1
            return res

        dict = defaultdict(int)
        dict[0] = 1
        return helper(root)

    # 936s
    # O(n^2)
    # recursion, start root, then make root.left "root", so have to call self.pathSum function not dfs function.
    def pathSum2(self, root, sum):
        def dfs2(root, sum):
            if not root: return 0
            print(f"root={root.val}, sum={sum}")
            count = 0
            if root.val == sum:
                count += 1
                print(f"count={count}")
            count += dfs2(root.left, sum-root.val)
            count += dfs2(root.right, sum-root.val)
            return count

        if not root: return 0
        return dfs2(root, sum) + self.pathSum2(root.left, sum) + self.pathSum2(root.right, sum)

    def pathSum4(self, root, sum):
        def helper(node, target):
            stack = [(root, sum)]
            count = 0

            while stack:
                node, target = stack.pop()

                print(f"node={node.val}, target={target}")
                target -= node.val
                if target == 0:
                    count += 1

                if node.left: stack.append((node.left, target))
                if node.right: stack.append((node.right, target))

            return count

        if not root: return 0
        return helper(root, sum) + self.pathSum4(root.left, sum) + self.pathSum4(root.right, sum)

    # 44s
    # https://leetcode.com/problems/path-sum-iii/discuss/91878/17-ms-O(n)-java-Prefix-sum-method
    # This is an excellent idea and took me some time to figure out the logic behind.
    # Hope my comment below could help some folks better understand this solution.
    #
    # The prefix stores the sum from the root to the current node in the recursion
    # The map stores <prefix sum, frequency> pairs before getting to the current node. We can imagine a path from the root to the current node.
    # The sum from any node in the middle of the path to the current node = the difference
    # between the sum from the root to the current node and the prefix sum of the node in the middle.
    # We are looking for some consecutive nodes that sum up to the given target value,
    # which means the difference discussed in 2. should equal to the target value.
    # In addition, we need to know how many differences are equal to the target value.
    # Here comes the map. The map stores the frequency of all possible sum in the path to the current node.
    # If the difference between the current sum and the target value exists in the map,
    # there must exist a node in the middle of the path, such that from this node to the current node, the sum is equal to the target value.
    # Note that there might be multiple nodes in the middle that satisfy what is discussed in 4.
    # The frequency in the map is used to help with this.
    # Therefore, in each recursion, the map stores all information we need to calculate the number of ranges that sum up to target.
    # Note that each range starts from a middle node, ended by the current node.
    # To get the total number of path count, we add up the number of valid paths ended by EACH node in the tree.
    # Each recursion returns the total count of valid paths in the subtree rooted at the current node. And this sum can be divided into three parts:
    # - the total number of valid paths in the subtree rooted at the current node's left child
    # - the total number of valid paths in the subtree rooted at the current node's right child
    # - the number of valid paths ended by the current node
    # The interesting part of this solution is that the prefix is counted from the top(root) to the bottom(leaves), and the result of total count is calculated from the bottom to the top :D
    #
    # The code below takes 16 ms which is super fast.
    def pathSum222(self, root, sum):
        from collections import defaultdict
        def findPS(curr, sum, target):
            if not curr: return 0
            sum += curr.val
            numPathToCurr = dict[sum-target]
            dict[sum] += 1
            print(f"curr={curr.val}, sum={sum}, numPathToCurr={numPathToCurr}, dict={dict}")

            res = numPathToCurr + findPS(curr.left, sum, target) + findPS(curr.right, sum, target)
            print(f"*res={res}, curr={curr.val},dict={dict}")
            dict[sum] = dict[sum] - 1
            print(f"**dict={dict}")
            return res

        if not root: return 0
        dict = defaultdict(int)
        dict[0] = 1
        return findPS(root, 0, sum)


    # https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
    def pathSum4(self, root, target):
        self.numOfPaths = 0
        self.dfs(root, target)
        return self.numOfPaths

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        if node is None: return

        print(f"[dfs] node.val = {node.val}, target={target}")
        self.findSum(node, target)  # you can move the line to any order, here is pre-order

        print(f"[dfs] after findSum node={node.val}, target={target}, call left")
        self.dfs(node.left, target)
        print(f"[dfs] after left dfs node={node.val}, target={target}, call right")
        self.dfs(node.right, target)
        print(f"[dfs] after right dfs")

    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def findSum(self, node, target):
        # exit condition
        if node is None:
            print(f"  return")
            return
        print(f" [findSum] node={node.val}, target={target}")
        if node.val == target:
            self.numOfPaths += 1
            print(f"   [findSum] self.numOfPaths={self.numOfPaths}")

        # test break down
        print(f" [findSum] call left test node={node.val}, target={target}")
        self.findSum(node.left, target - node.val)
        print(f" [findSum] call right test node={node.val}, target={target}")
        self.findSum(node.right, target - node.val)
        print(f" [findSum] after findSum node={node.val}, target={target}")

    # https://leetcode.com/problems/path-sum-iii/discuss/170367/Python-solution
    def pathSum5(self, root, sum):
        from collections import defaultdict
        def dfs(root, prevSum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            print(f"root={root.val}, prevSum={prevSum}, sum={sum}, currSum={currSum}, rec={rec}")
            if currSum - sum in rec:
                count += rec[currSum - sum]
            rec[currSum] += 1
            # if currSum in rec:
            #     rec[currSum] += 1
            # else:
            #     rec[currSum] = 1

            count += dfs(root.left, currSum)
            count += dfs(root.right, currSum)
            rec[currSum] -= 1
            print(f"rec={rec}, count={count}")
            return count

        rec = defaultdict(int)
        rec[0] = 1
        # rec = {0: 1}
        return dfs(root, 0)

nums = [10,5,-3,3,2,None,11,3,-2,None,1]
sum = 8

# nums=[30,20,10,5]
# sum=50
obj = Solution()
root = obj.buildTree(nums)
print(f"rtn :", obj.pathSum2(root, sum))
'''
    # https://leetcode.com/problems/path-sum-iii/discuss/170367/Python-solution
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        def dfs(root, prevSum, sum):
            if not root:
                return
            print(f"root={root.val}, prevSum={prevSum}, sum={sum}")

            currSum = prevSum + root.val
            print(f"currSum={currSum}, currSum - sum={currSum - sum}, rec={rec}")
            if currSum - sum in rec:
                self.count += rec[currSum - sum]
                print(f"self.count={self.count}")

            if currSum in rec:
                rec[currSum] += 1
                print(f"(aa) rec={rec}")
            else:
                rec[currSum] = 1
                print(f"(bb) rec={rec}")
            dfs(root.left, currSum, sum)
            dfs(root.right, currSum, sum)
            rec[currSum] -= 1

        self.count = 0
        rec = {0: 1}
        dfs(root, 0, sum)
        return self.count

    def pathSum2(self, root, sum):

        def dfs(root, prevSum, sum):
            if not root:
                return 0
            count = 0
            currSum = prevSum + root.val
            if currSum - sum in rec:
                count += rec[currSum - sum]
            if currSum in rec:
                rec[currSum] += 1
            else:
                rec[currSum] = 1
            count += dfs(root.left, currSum, sum)
            count += dfs(root.right, currSum, sum)
            rec[currSum] -= 1
            return count

        rec = {0: 1}
        return dfs(root, 0, sum)

    # def pathSum3(self, root, target):
    #     # define global result and path
    #     self.result = 0
    #     cache = {0: 1}
    #
    #     # recursive to get result
    #     self.dfs(root, target, 0, cache)
    #
    #     # return result
    #     return self.result
    #
    # def dfs(self, root, target, currPathSum, cache):
    #     # exit condition
    #     if root is None:
    #         return
    #         # calculate currPathSum and required oldPathSum
    #     print(f"root={root.val}, target={target}, currPathSum={currPathSum}, cache={cache}")
    #     currPathSum += root.val
    #     oldPathSum = currPathSum - target
    #     print(f"currPathSum={currPathSum}, oldPathSum={oldPathSum}")
    #     # update result and cache
    #     self.result += cache.get(oldPathSum, 0)
    #     cache[currPathSum] = cache.get(currPathSum, 0) + 1
    #     print(f"self.result={self.result}, cache={cache}")
    #
    #     # dfs breakdown
    #     print(f"call left")
    #     self.dfs(root.left, target, currPathSum, cache)
    #     print(f"call right target={target}, currPathSum={currPathSum}, cache={cache}")
    #     self.dfs(root.right, target, currPathSum, cache)
    #     print(f"end of call right - target={target}, currPathSum={currPathSum}, cache={cache}")
    #     # when move to a different branch, the currPathSum is no longer available, hence remove one.
    #     cache[currPathSum] -= 1
    #     print(f"cache[currPathSum]={cache[currPathSum]}")

    def pathSum4(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return
            # dfs break down
        print(f"[dfs] node.val = {node.val}, target={target}")
        self.test(node, target)  # you can move the line to any order, here is pre-order

        print(f"[dfs] after test")
        print(f"node={node.val}, target={target}, call left")
        self.dfs(node.left, target)
        print(f"node={node.val}, target={target}, call right")
        self.dfs(node.right, target)
        print(f"[dfs] after dfs")


    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        print(f"test node={node.val}, target={target}")
        if node.val == target:
            self.numOfPaths += 1
            print(f"self.numOfPaths={self.numOfPaths}")

        # test break down
        print(f"call left test node={node.val}, target={target}")
        self.test(node.left, target - node.val)
        print(f"call right test node={node.val}, target={target}")
        self.test(node.right, target - node.val)
        print(f"after test node={node.val}, target={target}")
'''