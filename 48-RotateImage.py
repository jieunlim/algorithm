# 48. Rotate Image

# n*n matrix time complexity O(n^2)
# space O(1)

class Solution:
    def rotate(self, matrix):

        if not matrix: return

        n = len(matrix[0])

        for i in range(n):
            k = m = n-i-1
            for j in range(i, n-i-1):
                print(f"i={i}, j={j}, k={k}")
                print(f"  {matrix[i][j]}, {matrix[j][m]}, {matrix[m][k]}, {matrix[k][i]}")

                matrix[i][j], matrix[j][m], matrix[m][k], matrix[k][i] = \
                    matrix[k][i], matrix[i][j], matrix[j][m], matrix[m][k]

                print(f"  {matrix[i][j]}, {matrix[j][m]}, {matrix[m][k]}, {matrix[k][i]}")
                k -= 1

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# matrix = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]
obj = Solution()
obj.rotate(matrix)
print(matrix)


'''
class Solution {
    public void rotate(int[][] matrix) {
        int len = matrix.length;
        
        for (int i=0; i<len/2; i++) {
            for(int j=0; j<(len+1)/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[len - 1 - j][i];
                matrix[len -1 -j][i] = matrix[len - 1 -i][len - 1 -j];
                matrix[len -1 -i][len -1 -j] = matrix[j][len -1 -i];
                matrix[j][len -1 -i] = temp;
            }
        }
    }
}
'''