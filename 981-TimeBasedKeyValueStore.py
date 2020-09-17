
# 981. Time Based Key-Value Store
# Hashmap, Binary Search?
class TimeMap(object):

    def __init__(self):
        import collections
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        import bisect

        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""

# Input: inputs = ["TimeMap","set","get","get","set","get","get"],
# inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
obj = TimeMap()
input1=["foo","bar",1]
# obj.set(key,value,timestamp)
obj.set(input1[0],input1[1],input1[2])
param_2 = obj.get(input1[0],input1[2])
print(param_2)