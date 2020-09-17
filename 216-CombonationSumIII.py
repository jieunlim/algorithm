
# 216. Combination Sum III


class Solution:
    def combinationSum3(self, k, n):

        def helper(n, path, idx):
            if n == 0 and len(path) == k:
                res.append(path[:])

            for i in range(idx, 10):
                if i > n: break
                helper(n - i, path + [i], i+1)

        res = []
        helper(n, [], 1)
        return res

    # k=3
    # n=7
    # print(combinationSum3(k, n))


    def combinationSum33(self, k: int, n: int) -> List[List[int]]:
        res = []
        k = k
        candidates = [x for x in range(1, 10)]

        def dfs(start, path, target, candidates):

            if target == 0 and path not in res and len(path) == k:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):

                if candidates[i] > target:
                    return

                path.append(candidates[i])
                dfs(i + 1, path, target - candidates[i], candidates)
                path.pop()

        dfs(0, [], n, sorted(candidates))
        return res

    def combinationSum333(self, k, n):

        def CS(t, path, idx):
            print(f"t={t}, path={path}, idx={idx}")
            if t == 0 and len(path) == 3:
                res.append(path)

            for i in range(idx, 10):
                if i > t: break
                CS(t-i, path + [i], i + 1)

        res = []
        CS(n, [], 1)
        return res

k = 3
n = 7
obj = Solution()
print(obj.combinationSum3(k, n))