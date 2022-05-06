# S: O(r+c), T: O(1)

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        r, c = 0, cols-1
        lastIdx = -1
        while c>=0 and r < rows:
            if binaryMatrix.get(r,c):
                lastIdx = c
                c-=1
            else: r += 1
        return lastIdx
        
