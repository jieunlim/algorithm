class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) < numRows:
            return s

        # rows = ['']*numRows
        rows = ['' for _ in range(numRows)]
        # ['','','']
        print(rows)

        i, step = 0, 0
        for c in s:
            rows[i] += c
            print(rows)
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1

            i += step
        return ''.join(rows)



