# 322. Coin Change
MAX = float('inf')
class Solution:
    def coinChange(self, coins, amount):
        def helper(target):

            print(f"target={target}, memo = {memo}")
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            minCnt = float('inf')
            for i in range(len(coins)):
                print(f"i = {i}")
                if target >= coins[i]:
                    cnt = helper(target - coins[i]) + 1
                    print(f"i = {i}, cnt={cnt}")
                    minCnt = min(minCnt, cnt)

            memo[target] = minCnt
            print(f"memo[target]={memo[target]}")
            return memo[target]

        # coins.sort()
        memo = {}
        rtn = helper(amount)
        return -1 if rtn == float('inf') else rtn

    # 160ms
    # https://leetcode.com/problems/coin-change/discuss/77438/Java-recursive-solution-3ms
    # recursion
    def __init__(self):
        self.total = MAX

    def coinChange2(self, coins, amount):
        def count(amount, idx, cnt):
            print(f"amount={amount}, idx={idx}, cnt={cnt}")
            if idx < 0 or cnt >= self.total-1:
                print(f"return")
                return

            curCoinCnt = amount//coins[idx]
            print(f"coins[idx]={coins[idx]}, curCoinCnt={curCoinCnt}")
            for i in range(curCoinCnt, -1, -1):
                newCnt = cnt + i
                newAmt = amount - i*coins[idx]
                print(f"  i={i}, newCnt={newCnt}, newAmt={newAmt}, coins[idx]={coins[idx]}")

                if newAmt == 0 and newCnt < self.total:
                    self.total = newCnt
                    print(f"  self.total = {self.total}")
                elif newCnt >= self.total - 1:
                    print(f"  break, newCnt{newCnt} >= self.total{self.total} - 1")
                    break
                else:
                    print(f"  call count")
                    count(newAmt, idx-1, newCnt)
                    print(f"  after count i={i}, newCnt={newCnt}, newAmt={newAmt}")

                # if newAmt > 0 and newCnt < self.total:
                #     print(f"  call count")
                #     count(newAmt, idx-1, newCnt)
                # elif newCnt < self.total:
                #     self.total = newCnt
                #     print(f"  self.total={self.total}")
                # elif newCnt >= self.total - 1:
                #     print(f"  break, newCnt{newCnt} >= self.total{self.total} - 1")
                #     break

        coins.sort()
        print(f"coins={coins}, amount={amount}")
        count(amount, len(coins)-1, 0)
        print(f"self.total={self.total}")
        return -1 if self.total == MAX else self.total

    # O(S*n)
    # 1532ms
    def coinChange3(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        print(f"dp = {dp}")
        for i in range(1, amount + 1):
            for coin in coins:
                print(f"i={i}, coin={coin}")
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    print(f"dp={dp}")
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

    def coinChange33333(self, coins, amount):

        def coinRe(amt):
            print(f"amt = {amt}")

            if amt < 0: return -1
            if amt == 0: return 0
            if amt-1 in memo: return memo[amt-1]

            minVal = MAX
            for coin in coins:
                print(f"coin = {coin}")
                if amt - coin >= 0:
                    res = coinRe(amt - coin) + 1
                    print(f"res={res}")
                    if res < minVal and res >= 0:
                        minVal = 1 + res
            memo[amt-1] = minVal if minVal != MAX else -1
            print(f"memo={memo}")
            return memo[amt-1]

        MAX = float('inf')
        memo = {}
        return coinRe(amount)

coins = [2, 3]
amount = 7
coins = [2, 3, 5]
amount = 13
# coins = [186,419,83,408]
# amount = 6249
obj = Solution()
print(obj.coinChange(coins, amount))

'''
        MAX = float('inf')
        self.total = MAX
        
        def count(amount, idx, cnt):
            if idx < 0 or cnt >= self.total-1: return

            curCoinCnt = amount//coins[idx]
            for i in range(curCoinCnt, -1, -1):
                newCnt = cnt + i
                newAmt = amount - i*coins[idx]
                if newAmt == 0 and newCnt < self.total:
                    self.total = newCnt
                elif newCnt >= self.total - 1:
                    break 
                else:
                    count(newAmt, idx-1, newCnt)
                    
                # if newAmt > 0 and newCnt < self.total:
                #     count(newAmt, idx-1, newCnt)
                # elif newCnt < self.total:
                #     self.total = newCnt
                # elif newCnt >= self.total - 1:
                #     break

        coins.sort()
        count(amount, len(coins)-1, 0)
        return -1 if self.total == MAX else self.total 
        
'''
'''
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #         def dfs(target, path, idx, minCnt):

        #             if not target:
        #                 return min(minCnt, len(path))
        #             else:
        #                 for i, val in enumerate(coins[idx:]):
        #                     if val > target:
        #                         continue
        #                     else:
        #                         minCnt = dfs(target - val, path + [val], idx + i, minCnt)

        #             return minCnt

        #         minCnt = float('inf')
        #         coins.sort(reverse=True)
        #         rCnt = dfs(amount, [], 0, minCnt)

        #         return rCnt if rCnt != float('inf') else -1

        def dfs(target, path, idx, minCnt):
            # print(f"target={target}, path={path}, idx={idx}, minCnt={minCnt}")
            if not target:
                # print(f"min({minCnt}, {len(path)}_")
                # return min(minCnt, len(path))
                return len(path)
            else:
                for i, val in enumerate(coins[idx:]):
                    # print(f"i={i}, val={val}, idx={idx}")
                    if val > target:
                        continue
                    else:
                        # minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        if minCnt != float('inf'):
                            return minCnt

            return minCnt

        minCnt = float('inf')
        coins.sort(reverse=True)
        rCnt = dfs(amount, [], 0, minCnt)

        return rCnt if rCnt != float('inf') else -1


'''

'''
# Time Limit Exceeded
# coins=[3,7,405,436]
# amount = 8839

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(target, path, idx, minCnt):
            print(f"target={target}, path={path}, idx={idx}, minCnt={minCnt}")
            if not target:
                # print(f"min({minCnt}, {len(path)}_")
                # return min(minCnt, len(path))
                return len(path)
            else:
                for i, val in enumerate(coins[idx:]):
                    print(f"i={i}, val={val}, idx={idx}")
                    if val > target:
                        continue
                    else:
                        # minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        if minCnt != float('inf'):
                            return minCnt

            return minCnt

        minCnt = float('inf')
        coins.sort(reverse=True)
        print(f"coins={coins}")
        rCnt = dfs(amount, [], 0, minCnt)

        return rCnt if rCnt != float('inf') else -1

'''



'''
# 322. Coin Change

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {0: 0}
        self.helper(amount, coins, min(coins), mem)
        return -1 if mem[amount] == float('inf') else mem[amount]

    def helper(self, amount, coins, m_c, mem):
        print(f"amount={amount}, m_c={m_c}, mem={mem}")
        if amount in mem:
            print(f"return mem {mem[amount]}")
            return mem[amount]
        mem[amount] = min([self.helper(amount - c, coins, m_c, mem) for c in coins]) + 1 if amount >= m_c else float(
            'inf')
        return mem[amount]

    def coinChange2(self, coins, amount):
        from collections import defaultdict
        def coinRe(idx, amt, cnt, minCnt):
            print(f"idx={idx}, amt={amt}, cnt={cnt}, minCnt={minCnt}, memo={memo}")

            if amt in memo:
                print(f"return memo {memo[amt]}")
                return memo[amt]

            if not amt:
                minCnt = min(minCnt, cnt)
                memo[amt] = minCnt #if memo[amt] > minCnt else MAX
                print(f"return minCnt={minCnt}")
                return memo[amt]

            for i, coin in enumerate(coins[idx:]):
                if coin <= amt:
                    print(f"coin={coin}, amt={amt}")
                    minCnt = coinRe(i+idx, amt - coin, cnt+1, minCnt)

            return minCnt

        MAX = float('inf')
        minCnt = MAX
        coins.sort(reverse=True)
        memo = defaultdict(int)
        rCnt = coinRe(0, amount, 0, minCnt)

        return rCnt if rCnt != MAX else -1


coins = [1,2,5]
amount = 11
# coins=[3,7,405,436]
# amount = 8839
# coins=[2]
# amount = 3
obj = Solution2()
print(obj.coinChange(coins, amount))


'''



''' 
class Solution:
    def coinChange(self, coins, amount):
        #         def dfs(target, path, idx, minCnt):

        #             if not target:
        #                 return min(minCnt, len(path))
        #             else:
        #                 for i, val in enumerate(coins[idx:]):
        #                     if val > target:
        #                         continue
        #                     else:
        #                         minCnt = dfs(target - val, path + [val], idx + i, minCnt)

        #             return minCnt

        #         minCnt = float('inf')
        #         coins.sort(reverse=True)
        #         rCnt = dfs(amount, [], 0, minCnt)

        #         return rCnt if rCnt != float('inf') else -1

        def dfs(target, path, idx, minCnt):
            print(f"target={target}, path={path}, idx={idx}, minCnt={minCnt}")
            if not target:
                print(f"min={minCnt}, {len(path)}")
                # return min(minCnt, len(path))
                return len(path)
            else:
                for i, val in enumerate(coins[idx:]):
                    print(f"i={i}, val={val}, idx={idx}")
                    if val > target:
                        continue
                    else:
                        # minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        minCnt = dfs(target - val, path + [val], idx + i, minCnt)
                        if minCnt != float('inf'):
                            return minCnt

            return minCnt

        minCnt = float('inf')
        coins.sort(reverse=True)
        rCnt = dfs(amount, [], 0, minCnt)

        return rCnt if rCnt != float('inf') else -1


coins = [2, 3]
amount = 7

coins=[186,419,83,408]
amount = 6249
obj = Solution()
print(obj.coinChange(coins, amount))
 
 
def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]
        # print(f"dp = {dp}")
        for i in range(1, amount + 1):
            for coin in coins:
                # print(f"i={i}, coin={coin}")
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    # print(f"dp={dp}")
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

    
#     Accecpted
#         mem = {0: 0}
#         self.helper(amount, coins, min(coins), mem)
#         return -1 if mem[amount] == float('inf') else mem[amount]

#     def helper(self, amount, coins, m_c, mem):
#         # print(f"amount={amount}, m_c={m_c}, mem={mem}")
#         if amount in mem:
#             # print(f"return mem {mem[amount]}")
#             return mem[amount]
#         mem[amount] = min([self.helper(amount - c, coins, m_c, mem) for c in coins]) + 1 if amount >= m_c else float(
#             'inf')
#         # print(f"amount={amount}, mem[{amount}]={mem[amount]}")
#         return mem[amount]
    

    
# #     [3,7,405,436]
# # 8839
# # TLE
#         def dfs(target, path, idx, minCnt):
            
#             if not target: 
#                 return min(minCnt, len(path))
#             else:
#                 for i, val in enumerate(coins[idx:]):
#                     if val > target:
#                         continue
#                     else:
#                         minCnt = dfs(target - val, path + [val], idx + i, minCnt)

#             return minCnt 
        
#         minCnt = float('inf')
#         coins.sort(reverse=True) 
#         rCnt = dfs(amount, [], 0, minCnt) 
        
#         return rCnt if rCnt != float('inf') else -1


# #         wrong answer
# # [186,419,83,408]
# # 6249
# # expected 20
#         from collections import defaultdict
#         def coinRe(idx, amt, cnt, minCnt):
#             # print(f"idx={idx}, amt={amt}, cnt={cnt}, minCnt={minCnt}, memo={memo}")

#             if amt in memo:
#                 # print(f"return memo {memo[amt]}")
#                 return memo[amt]

#             if not amt:
#                 minCnt = min(minCnt, cnt)
#                 memo[amt] = minCnt #if memo[amt] > minCnt else MAX
#                 # print(f"return minCnt={minCnt}")
#                 return memo[amt]

#             for i, coin in enumerate(coins[idx:]):
#                 if coin <= amt:
#                     # print(f"coin={coin}, amt={amt}")
#                     minCnt = coinRe(i+idx, amt - coin, cnt+1, minCnt)

#             return minCnt

#         MAX = float('inf')
#         minCnt = MAX
#         coins.sort(reverse=True)
#         memo = defaultdict(int)
#         rCnt = coinRe(0, amount, 0, minCnt)
        
#         return rCnt if rCnt != MAX else -1
    
    
    
# [186,419,83,408]
# 6249
# Wrong answer
#         def dfs(target, path, idx, minCnt):
#             # print(f"target={target}, path={path}, idx={idx}, minCnt={minCnt}")
#             if not target:
#                 # print(f"min({minCnt}, {len(path)}_")
#                 # return min(minCnt, len(path))
#                 return len(path)
#             else:
#                 for i, val in enumerate(coins[idx:]):
#                     # print(f"i={i}, val={val}, idx={idx}")
#                     if val > target:
#                         continue
#                     else:
#                         # minCnt = dfs(target - val, path + [val], idx + i, minCnt)
#                         minCnt = dfs(target - val, path + [val], idx + i, minCnt)
#                         if minCnt != float('inf'):
#                             return minCnt

#             return minCnt

#         minCnt = float('inf')
#         coins.sort(reverse=True) 
#         rCnt = dfs(amount, [], 0, minCnt)

#         return rCnt if rCnt != float('inf') else -1
 

'''