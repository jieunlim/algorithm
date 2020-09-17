# 1130. Minimum Cost Tree From Leaf Values

class Solution:
    # DP
    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/340004/Python-Easy-DP
    # O(N^3)
    # When we check root, we find that the value of root only depends on how we divide the left arr and right arr.
    # Thus dp(i,j) = dp(i,k) + dp(k+1,j) + value of root.

    def mctFromLeafValues(self, arr):
        def dp(i, j):
            print(f"i={i}, j={j}, memo={memo}")
            if i >= j: return 0

            if (i, j) in memo:
                return memo[(i, j)]

            res = float('inf')
            for k in range(i + 1, j + 1):
                print(f"    i={i}, k={k}, j={j}")
                sumOfNleaf = dp(i, k - 1) + dp(k, j)
                sumOfroot = max(arr[i:k]) * max(arr[k:j + 1])
                res = min(res, sumOfNleaf + sumOfroot)
                print(f"    sumOfNleaf={sumOfNleaf}, sumOfroot={sumOfroot}, res={res}")

            memo[(i, j)] = res
            return memo[(i, j)]

        memo = {}
        return dp(0, len(arr) - 1)

    # Mathmatical O(n)
    # https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/340014/Greedy-python-solution
    # Pick up the leaf node with minimum value.
    # Combine it with its inorder neighbor which has smaller value between neighbors.
    # Once we get the new generated non-leaf node, the node with minimum value is useless
    # (For the new generated subtree will be represented with the largest leaf node value.)
    # Repeat it until there is only one node.
    def mctFromLeafValues1(self, arr):
        res = 0
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            print(f"mini_idx={mini_idx}, arr={arr}")
            if 0 < mini_idx < len(arr) - 1:
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
                print(f"A res={res}")
            else:
                res += arr[1 if mini_idx == 0 else mini_idx - 1] * arr[mini_idx]
                print(f"B res={res}")
            arr.pop(mini_idx)
        return res


arr = [6, 2, 4]
# arr=[1,2,3,4,5]
arr=[5,4,2,3]
obj = Solution()
print(obj.mctFromLeafValues(arr))