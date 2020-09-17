# 746. Min Cost Climbing Stairs
class Solution(object):
    #copid from solution
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)

# recursion top down
    def min_cost_climb_stairs(self, cost):

        def mcsc_re(i):

            if i < 2:
                return cost[i]

            return min( mcsc_re(i-1), mcsc_re(i-2)) +cost[i]

        return min(mcsc_re(len(cost)-1), mcsc_re(len(cost)-2))

    def min_cost_climb_stairs3(self, cost):

        def minCCS(i):
            print(f"i={i}, memo={memo}")
            # if i < 2:
            #     print(f"return {cost[i]}")
            #     return cost[i]
            if i < 0:
                return 0

            if i in memo:
                print(f"return memo {memo[i]}")
                return memo[i]

            if i >= len(cost):
                c = 0
            else:
                c = cost[i]
            memo[i] = min(minCCS(i-1), minCCS(i-2)) + c
            print(f" memo[i]={memo[i]}, i={i}")
            return memo[i]

        memo = {}
        return minCCS(len(cost))

# recursion bottom up
    def min_cost_climb_stairs2(self, cost):

        def minCCS(i):
            print(f"i={i}, memo={memo}")
            if i >= len(cost):
                print(f"return")
                return 0

            if i in memo:
                print(f"return memo {memo[i]}")
                return memo[i]

            if i < 0:
                c = 0
            else:
                c = cost[i]

            print(f"c = {c}")
            memo[i] = min(minCCS(i+1), minCCS(i+2)) + c
            print(f" memo[i]={memo[i]}, i={i}")
            return memo[i]

        memo = {}
        return minCCS(-1)

cost = [10, 15, 20, 5]
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
obj = Solution()
# print(obj.minCostClimbingStairs3(cost))
print(obj.min_cost_climb_stairs3(cost))


# 70. Climbing Stairs
# 830. Positions of Large Groups
# 565. Array Nesting
# 1329. Sort the Matrix Diagonally

# 879. Profitable Schemes
# 898. Bitwise ORs of Subarrays
# 1151. Minimum Swaps to Group All 1's Together