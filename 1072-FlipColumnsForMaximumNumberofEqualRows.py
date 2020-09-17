
# 1072. Flip Columns For Maximum Number of Equal Rows
def maxEqualRows(matrix):
    from collections import defaultdict

    if not matrix: return 0
    dic = defaultdict(int)
    maxV = 0
    for i in range(len(matrix)):
        s, s2 = '', ''
        for j in range(len(matrix[0])):
            s += '1' if matrix[i][j] == 1 else '0'
            s2 += '1' if matrix[i][j] == 0 else '0'
        dic[s] += 1
        dic[s2] += 1

        maxV = max(maxV, dic[s], dic[s2])

    print(dic)
    # print(dic.items())
    return maxV

def maxEqualRows2(matrix):
    ans = 0
    m, n = len(matrix), len(matrix[0])
    visited = [0 for _ in range(m)]
    flip =  [0 for _ in range(n)]

    for i in range(m):
        print(f"i={i}, visited={visited}")
        print(f"matrix[i] = {matrix[i]}")
        if visited[i] == 1: continue
        cnt = 1
        for j in range(n):
            flip[j] = 1 - matrix[i][j]
        print(f"flip = {flip}, cnt={cnt}")

        for k in range(i+1, m):
            if visited[k] == 1: continue
            print(f"matrix[k] = {matrix[k]}")
            if matrix[k] == matrix[i] or matrix[k] == flip:
                cnt += 1
                visited[k] = 1

        ans = max(ans, cnt)
        print(f"ans={ans}, cnt={cnt}")
    return ans

matrix = [
    [0,0,0],
    [0,0,1],
    [1,1,0]]

print("rtn:", maxEqualRows2(matrix))

