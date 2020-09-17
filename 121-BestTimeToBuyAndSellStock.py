# 121. Best Time to Buy and Sell Stock
# O(n), O(1)
# We need to find the largest peak following the smallest valley.
# We can maintain two variables-minPrice and maxProfit corresponding to the smallest valley and maximum profit.
# Same as 53.Maximum Subarray

class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            print(f"*price={price}")
            min_price = min(min_price, price)
            print(f"min_price={min_price}")

            profit = price - min_price
            print(f"profit={profit}")

            max_profit = max(max_profit, profit)
            print(f"max_profit={max_profit}")
        return max_profit

prices=[7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))


# by MS
# 84 ms
# time O(N)
# space O(N)
def maxProfit2(prices):

    if not prices:
        return 0

    minArr = [0 for _ in range(len(prices))]
    maxArr = [0 for _ in range(len(prices))]
    rtn = 0

    minArr[0] = prices[0]
    maxArr[-1] = prices[-1]

    for i in range(1, len(prices)):
        minArr[i] = min(prices[i], minArr[i-1])

    print(minArr)
    for i in range(len(prices)-2, -1, -1):
        maxArr[i] = max(prices[i], maxArr[i+1])

    print(maxArr)
    for i in range(len(prices)):
        rtn = max(rtn, abs(maxArr[i]-minArr[i]))
        print(f"rtn ={rtn}, {maxArr[i]-minArr[i]}")

    return rtn

prices=[7,1,5,3,6,4]
prices=[]
print(maxProfit(prices))

# 122. Best Time to Buy and Sell Stock II
# 123. Best Time to Buy and Sell Stock III
# 188. Best Time to Buy and Sell Stock IV
# 309. Best Time to Buy and Sell Stock with Cooldown