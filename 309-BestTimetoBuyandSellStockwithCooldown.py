# 309. Best Time to Buy and Sell Stock with Cooldown
# buy-sell-cooldown
# You must sell the stock before you buy again
# After you sell your stock, you cannot buy stock on next day

class Solution:
# time O(n^2), space O(n)

    def maxProfit(self, prices):

        length = len(prices)
        maxP = [0] * (length+2)

        for i in range(length-1, -1, -1): # ith day- buying or not
            # in case buying, find selling day to maximize profit
            curMaxProfit = 0
            for sellDay in range(i+1, length):
                curProfit = prices[sellDay] - prices[i] + maxP[sellDay+2] #selling profit on 'sellDay' + profit on 2 days after
                curMaxProfit = max(curMaxProfit, curProfit)
            # in case do nothing, choose which is better
            maxP[i] = max(maxP[i+1], curMaxProfit)

        return maxP[0]


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/293789/Python-O(N)-DP-I-believe-my-state-is-easier-to-understand
# Use DP to solve this problem. It is obviously to come up with DP, because this is a "stage-decision-problem", every day we decide buy/sell/rest.
#
# The state is defined as below
#
# dp(n, 0) -> The max profix we get on day n, if we rest on day n.
# dp(n, 1) -> The max profix we get on day n, if we buy on day n.
# dp(n, 2) -> The max profix we get on day n, if we sell on day n.
#
# Below is the state transition function
#
# dp(n, 0) = max{ dp(n-1, 1), dp(n-1, 0), dp(n-1, 2) },
#   if we rest on day n, we do not really care about what we have done on day n-1,
#   you can do whatever you want, and we just take the max profit from day n-1
# dp(n, 1) = dp[n-1][0] - prices[n],
#   if we buy on day n, we cannot buy on day n-1, because double-buy is by natural disallowed
#   in the "Stock" Series. We cannot sell on day n-1, because of the new cool-down policy.
#   So in day n-1, we can only rest.
# dp(n, 2) = max {dp(0, 1), dp(1, 1), ...., dp(n-1, 1)} + prices[n],
#   if we sell on day n, we need to make sure we buy the stock before in one of (0...n-1).
#   For example, if you rest on the first 2 days, there is NOTHING for you to sell on the 3rd day.
#   Among all the possible "buy-day", we pick the one with max-profix
# Now, you might think: hmmmm, this is an O(N^2) DP because of 3.,
# we need to get max from a list of values in each iteration.
# Not really, you can keep track of the max of the past dp(n, 1).
# In the following solution, I use the var bought to keep track.

    def maxProfit2(self, prices):
        if not prices:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float('-inf')
        bought = dp[0][1]

        n = len(prices)
        for i in range(1, n):
            dp[i][0] = max([dp[i - 1][0], dp[i - 1][2], dp[i - 1][1]])
            dp[i][1] = dp[i - 1][0] - prices[i]
            dp[i][2] = bought + prices[i]

            bought = max(bought, dp[i][1])
            print(f"bought={bought}")
            print(dp)
        return max(dp[n - 1])

obj = Solution()
prices = [10,20,30,0,20]
prices = [30,40,50,10,20,70]
print(obj.maxProfit(prices))


# goot to read
# https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323