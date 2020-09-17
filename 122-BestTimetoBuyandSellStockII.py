# 122. Best Time to Buy and Sell Stock II

class Solution:
    # Simple One Pass
    # time O(N), sapce O(1)
    def maxProfit(self, prices):
        total = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                total += prices[i + 1] - prices[i]
                print(f"total={total}, prices[i]={prices[i]}, prices[i + 1]={prices[i + 1]}")
        return total

    # Peak Valley Approach
    # time O(N), sapce O(1)
    def maxProfit2(self, prices):
        maxProfit, i = 0, 0

        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            print(f" i={i}, valley={valley}")
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            print(f" i={i}, peak={peak}")
            maxProfit += peak - valley
            print(f" maxProfit={maxProfit}")
        return maxProfit

obj = Solution()
prices = [1, 2, 1, 2, 5, 9]
print(obj.maxProfit2(prices))


# https://medium.com/algorithms-and-leetcode/best-time-to-buy-sell-stocks-on-leetcode-the-ultimate-guide-ce420259b323
