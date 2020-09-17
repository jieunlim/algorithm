# 339. Nested List Weight Sum

# DFS
# O(N) - N is the total number of nested elements, which is the number of items the algorithm has to iterate in total
# O(D) - D is maximum depth, which is times we call the function
# The algorithm takes O(N) time, where N is the total number of nested elements in the input list. For example, the list
# [ [[[[1]]]], 2 ] contains nested lists and nested integers and so N=6
# In terms of space, at most O(D) recursive calls are placed on the stack,
# where D is the maximum level of nesting in the input. For example ,
# D=2 for the input [[1,1],2,[1,1]], and D=3 for the input [1,[4,[6]]].

from typing import List
class Solution:
    def depthSum2(self, nestedList):

        if len(nestedList) == 0: return 0
        stack, sum = [], 0
        for n in nestedList:
            stack.append((n, 1))

        while stack:
            next, d = stack.pop(0)
            if next.isInteger():
                sum += d*next.getInteger()
            else:
                for i in next.getList():
                    stack.append(i, d+1)
        return sum

    def depthSum(self, nestedList):

        def helper(nList, depth, res):
            for item in nList:
                if isinstance(item, int):
                    res += item*depth
                else:
                    res += helper(item, depth+1, 0)
            return res

        return helper(nestedList, 1, 0)

obj = Solution()
nestedList = [1, [1, 1]]
nestedList = [[1,1],2,[1,1]]
print(obj.depthSum(nestedList))

# print(isinstance(nestedList[0], int))



# https://nifannn.github.io/2018/09/10/Algorithm-Notes-Leetcode-339-Nested-List-Weight-Sum/

'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def helper(nList: List[NestedInteger], depth):
            sum = 0
            for item in nList:
                if item.isInteger():
                    sum += item.getInteger() * depth
                else:
                    sum += helper(item.getList(), depth+1)
        
            return sum
        
        return helper(nestedList, 1)
'''