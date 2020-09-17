# 134. Gas Station

# gas station [0,1,2,3,4]
# gas amount  [1,2,3,4,5]
# cost        [3,4,5,1,2]
#
# i -> i+1
class Solution:
    # O(N^2)
    def canCompleteCircuit(self, gas, cost):

        n = len(gas)

        for i in range(n):
            if cost[i] <= gas[i]:
                curGas = gas[i] - cost[i]
                start = i
                print(f"i={i}, curGas={curGas}, gas[i]={gas[i]}, cost[i]={cost[i]}")
                for j in range(i+1, i+n+1):
                    print(f"j={j}, j%n={j%n}, i+n+1={i+n+1}, curGas={curGas}")
                    if cost[j%n] > gas[j%n] + curGas:
                        break
                    elif j == i+n:
                        return start
                    curGas += gas[j%n] - cost[j%n]
        return -1

    def canCompleteCircuit2(self, gas, cost):
        n = len(gas)
        for i in range(n):
            curGas = gas[i] - cost[i]
            if curGas >= 0:
                print(f"i={i}, curGas={curGas}, gas[i]={gas[i]}, cost[i]={cost[i]}")
                for j in range(i+1, i+n+1):
                    pos = j%n
                    print(f"j={j}, j%n={j%n}, i+n+1={i+n+1}, curGas={curGas}")
                    curGas += gas[pos] - cost[pos]
                    if curGas < 0:
                        break
                if curGas >= 0: return i
        return -1

    def canCompleteCircuit3(self, gas, cost):
        n= len(gas)
        for i in range(n):
            sum = 0
            print(f"i={i}")
            for j in range(n):
                loc = (i+j)%n
                sum += gas[loc] - cost[loc]
                print(f" j={j}, loc={loc}, sum={sum}")
                if sum < 0: break
            if sum >= 0:
                return i
        return -1

    # One pass
    # O(N)
    # https://youtu.be/nTKdYm_5-ZY

    def canCompleteCircuit1(self, gas, cost):

        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            print(f"total_tank = {total_tank}, curr_tank={curr_tank}")
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                print(f"starting_station={starting_station}")
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    # class Solution {
    #     public int canCompleteCircuit(int[] gas, int[] cost) {
    #         int sum = 0;
    #         int min = gas[0] - cost[0];
    #         int minIndex = 0;
    #         for (int i=0; i<gas.length; i++) {
    #             sum = sum + gas[i] - cost[i];
    #             if (min > sum) {
    #                 min = sum;
    #                 minIndex = i;
    #             }
    #         }
    #         if (sum < 0) return -1;
    #         return (minIndex + 1)%cost.length;
    #     }
    # }

    def canCompleteCircuit11(self, gas, cost):
        sum = 0
        min = gas[0] - cost[0]
        minIdx = 0
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            if min>sum:
                min = sum
                minIdx = i
        if sum < 0: return -1
        print(f"minIdx={minIdx}")
        return (minIdx+1)%len(cost)

    def canCompleteCircuit12(self, gas, cost):
        minV = float('inf')
        totalGas = 0
        startIdx = -1

        for i in range(len(gas)):

            totalGas += gas[i] - cost[i]
            if minV > totalGas:
                minV = totalGas
                startIdx = i

        return (startIdx+1)%len(gas) if totalGas >= 0 else -1

gas=[3,1,1]
cost=[1,2,2]
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# gas  = [2,3,4]
# cost = [3,4,3]
# gas=[2]
# cost=[2]
obj = Solution()
print(obj.canCompleteCircuit11(gas, cost))

