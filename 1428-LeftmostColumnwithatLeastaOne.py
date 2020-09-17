# 1428. Leftmost Column with at Least a One

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
        leftMostCol = cols
        for row in range(rows):
            start, end = 0, cols - 1
            while start < end:
                mid = start + (end - start) // 2
                if binaryMatrix.get(row, mid) == 0:
                    start = mid + 1
                else:
                    end = mid
            if binaryMatrix.get(row, start) == 1:
                leftMostCol = min(leftMostCol, start)
        return leftMostCol if leftMostCol != cols else -1

    def leftMostColumnWithOne2(self, binaryMatrix: 'BinaryMatrix') -> int:
#         O(N*M)
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        print(f"rows={rows},cols={cols}")
        # Go through each of the rows.
        for row in range(rows):
            # Linear seach for the first 1 in this row.
            for col in range(cols):
                if binaryMatrix.get(row, col) == 1:
                    smallest_index = min(smallest_index, col)
                    break
        # If we found an index, we should return it. Otherwise, return -1.
        return -1 if smallest_index == cols else smallest_index


    # O(NLogM): N-rows, M-cols
    # O(1)
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            # Binary Search for the first 1 in the row.
            lo = 0
            hi = cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # If the last element in the search space is a 1, then this row
            # contained a 1.
            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        # If smallest_index is still set to cols, then there were no 1's in
        # the grid.
        return -1 if smallest_index == cols else smallest_index


    # https://www.youtube.com/watch?v=NEZn3XmiTWI
    # TC O(N+M)
    # O(N+M) > O(NLogM) if M is bigger number
    def leftMostColumnWithOne3(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        r = 0
        c = m-1
        last_c = -1
        while r < n and c >= 0:
            if binaryMatrix.get(r,c):
                last_c = c
                c -= 1
            else:
                r += 1
        return last_c

'''
   
        
        # n, m = binaryMatrix.dimensions()
        # r = 0
        # c = m-1
        # last_c = -1
        # while r < n and c >= 0:
        #     print(f"r={r}, c={c}")
        #     if binaryMatrix.get(r,c):
        #         last_c = c
        #         c -= 1
        #     else:
        #         r += 1
        # return last_c
    
        # rows, cols = binaryMatrix.dimensions()
        # smallest_index = cols
        # print(f"rows={rows},cols={cols}")
        # # Go through each of the rows.
        # for row in range(rows):
        #     # Linear seach for the first 1 in this row.
        #     for col in range(cols):
        #         if binaryMatrix.get(row, col) == 1:
        #             smallest_index = min(smallest_index, col)
        #             break
        # # If we found an index, we should return it. Otherwise, return -1.
        # return -1 if smallest_index == cols else smallest_index

    
    
    
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            # Binary Search for the first 1 in the row.
            lo = 0
            hi = cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                print(f"row={row}, mid={mid}, {binaryMatrix.get(row, mid)}, lo={lo}, hi={hi}")
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # If the last element in the search space is a 1, then this row
            # contained a 1.
            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        # If smallest_index is still set to cols, then there were no 1's in 
        # the grid. 
        return -1 if smallest_index == cols else smallest_index
'''