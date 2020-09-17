# 96. Unique Binary Search Trees
# Time O(N**2), Space O(N)
# DP
def numTrees(n):

    G = [0] * (n + 1)
    G[0], G[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]
            print(f"i={i}, j={j}, G[{i}]={G[i]}, G[{j - 1}]={G[j - 1]}, G[{i - j}]={G[i - j]}")

    # print(G)
    return G[n]

# # Catalan Number  (2n)!/((n+1)!*n!)
# def numTrees2(self, n):
#     return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))

def numTrees2(n):
    def getCount(size):
        if size in dic:
            return dic[size]
        ret = 0
        for i in range(len(size)):
            ret += getCount(i) * getCount(size-i-1)
        dic[size] = ret
        return ret

    dic = {0:1, 1:1, 2:2}
    return getCount(n)
n = 4
print(numTrees2(n))

'''
class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();
    
    int getCount(int size) {
        if (map.containsKey(size)) return map.get(size);
        int ret = 0;
        for (int i=0; i<size; i++) {
            int temp = map.getOrDefault(i, getCount(i));
            temp*= map.getOrDefault(size - i - 1, getCount(size - i - 1));
            ret += temp;
        }
        map.put(size, ret);
        return ret;
    }
    
    public int numTrees(int n) {
        map.put(0,1);
        map.put(1,1);
        map.put(2,2);
        return getCount(n);
    }
}
'''
# def numTree(n):
#     if n < 2:
#         return n
#
#     res = [0] * ( n + 1 )
#     res[0] = res[1] = 1
#
#     for i in range(2, n+1):
#         for j in range(1, i+1):
#             res[i] += res[j-1] * res[i-j]
#             print(res)
#
#     return res[n]
#
# n = 3
# print(numTree(n))