# 986. Interval List Intersections
# time O(M+N)
# space O(1)
# https://leetcode.com/problems/interval-list-intersections/discuss/231100/Python-short-O(m%2Bn)-solution
class Solution:
    def intervalIntersection(self, A, B):
        if not A or not B: return []
        start, end = 0, 1
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][end] < B[j][start]: i += 1
            elif A[i][start] > B[j][end]: j += 1
            else:
                res.append([max(A[i][start], B[j][start]), min(A[i][end], B[j][end])])
                if A[i][end] > B[j][end]: j += 1
                else: i += 1
        return res

    def intervalIntersection(self, A, B):

        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):

            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            print(A[i], B[j], start, end)
            if start <= end:
                result.append([start, end])

            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
                j += 1
        return result

    def intervalIntersection2(self, A, B):
        res = []
        i, j = 0, 0

        while i < len(A) and j < len(B):
            print(f"i={i}, j={j}")
            print(f"max({A[i][0]}, {B[j][0]})")
            print(f"min({A[i][1]}, {B[j][1]})")
            max0 = max(A[i][0], B[j][0])
            min1 = min(A[i][1], B[j][1])
            if max0 <= min1:
                res.append([max0, min1])
                print(f"res={res}")

            if A[i][1] > B[j][1]:
                j += 1
                print(f"j={j}")
            elif B[j][1] > A[i][1]:
                i += 1
                print(f"i={i}")
            else:
                i += 1
                j += 1
                print(f"i={i}, j={j}")

        return res

a=[[0,2],[5,10]]
b=[[1,5],[8,12]]

a = [[0,2],[5,10],[13,23],[24,25]]
b = [[1,5],[8,12],[15,24],[25,26]]

a = [[3,5],[9,20]]
b = [[4,5],[7,10],[11,12],[14,15],[16,20]]

obj = Solution()
print(obj.intervalIntersection(a, b))

# 56. Merge Intervals
# 88. Merge Sorted Array


# https://youtu.be/HFhvYBWQ1XA

# public int[][] intervalIntersection(int[][] A, int[][] B) {
#         ArrayList<int[]> arr = new ArrayList<>();
#         int Aindex = 0, Bindex = 0;
#         while(Aindex < A.length && Bindex < B.length) {
#             if (A[Aindex][1] < B[Bindex][0]) Aindex++;
#             else if (A[Aindex][0] > B[Bindex][1]) Bindex++;
#             else {
#                 int[] c = {Math.max(A[Aindex][0], B[Bindex][0]), Math.min(A[Aindex][1], B[Bindex][1])};
#                 arr.add(c);
#                 if (A[Aindex][1] > B[Bindex][1]) Bindex++;
#                 else Aindex++;
#             }
#         }
#         int [][] result = new int[arr.size()][2];
#         for (int i=0; i<arr.size(); i++) result[i] = arr.get(i);
#         return result;
#     }


