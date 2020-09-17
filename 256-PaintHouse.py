
# 256. Paint House
# time O(2**n), space O(n)
# https://leetcode.com/problems/paint-house/solution/

def minCost(costs):

    def paint_cost(n, color):

        print(f"n={n}, color={color}, costs={costs}")
        if (n, color) in memo:
            return memo[(n, color)]

        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0: # Red
            total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
        elif color == 1: # Green
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
        else: # Blue
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))

        memo[(n, color)] = total_cost
        print(f"  return n={n}, color={color}, total_cost={total_cost}")
        return total_cost

    if costs == []:
        return 0
    memo = {}
    return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

def minCost2(costs):
    import copy
    if len(costs) == 0: return 0

    previous_row = costs[-1]
    print(f"costs={costs}")
    for n in reversed(range(len(costs) - 1)):
        print(f"n={n}, previous_row={previous_row}")
        current_row = copy.deepcopy(costs[n])
        print(f"current_row={current_row}, costs[n]={costs[n]}")
        # Total cost of painting nth house red?
        current_row[0] += min(previous_row[1], previous_row[2])
        print(f"current_row[0]={current_row[0]}")
        # Total cost of painting nth house green?
        current_row[1] += min(previous_row[0], previous_row[2])
        print(f"current_row[1]={current_row[1]}")
        # Total cost of painting nth house blue?
        current_row[2] += min(previous_row[0], previous_row[1])
        print(f"current_row[2]={current_row[2]}")
        previous_row = current_row
        print(f"current_row={current_row}, previous_row={previous_row}")

    return min(previous_row)

# if len(costs) == 0: return 0
#
# previous_row = costs[-1]
# for n in reversed(range(len(costs) - 1)):
#
#     # PROBLEMATIC CODE IS HERE
#     # This line here is NOT making a copy of the original, it's simply
#     # making a reference to it Therefore, any writes into current_row
#     # will also be written into "costs". This is not what we wanted!
#     current_row = costs[n]
#
#     # Total cost of painting nth house red?
#     current_row[0] += min(previous_row[1], previous_row[2])
#     # Total cost of painting nth house green?
#     current_row[1] += min(previous_row[0], previous_row[2])
#     # Total cost of painting nth house blue?
#     current_row[2] += min(previous_row[0], previous_row[1])
#     previous_row = current_row
#
# return min(previous_row)


costs=[[17,2,17],[16,16,5],[14,3,19]]
print(minCost(costs))

# 213. House Robber II
# 265. Paint House II
# 276. Paint Fence
