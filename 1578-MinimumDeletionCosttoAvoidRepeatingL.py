# 1578. Minimum Deletion Cost to Avoid Repeating Letters

def minCost(s: str, cost: List[int]):

    rtn, c, ch = 0, 0, "."

    for i in range(len(s)):
        if ch != s[i]:
            ch = s[i]
            c = cost[i]
        else:
            rtn += min(c, cost[i])
            c = max(c, cost[i])
    return rtn