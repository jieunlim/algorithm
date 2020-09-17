# 1488. Avoid Flood in The City
# 1,2,0,1,0,2
#
# res = [-1, 1, 0, -1, -1, 2]
# list = {}
# dic = {1:3, 2:4,}
#
#
# 1,2,3,0,0,3,0,2
# res = [-1,-1,-1,3, 2, -1]
# zeros={}
# dic={1:0, 2:6, 3:5}
#

# finding zeros - minimum value of the smaller values than the lake index
def avoidFlood(self, rains: List[int]) -> List[int]:
    def getK(l, r):

        if len(zeros) < 1:
            return -1

        start, end = 0, len(zeros) - 1

        while start < end:
            mid = (start + end) // 2

            if l > zeros[mid]:
                start = mid + 1
            else:
                end = mid

                # print(f"zeros[start]={zeros[start]}, start={start}")
        if start < len(zeros) and zeros[start] > l:
            return zeros[start]
        else:
            return -1

    res = []
    zeros = []
    dic = {}
    for i, r in enumerate(rains):
        if r == 0:
            res.append(1)
            zeros.append(i)
        elif r > 0:
            res.append(-1)
            if r not in dic:
                dic[r] = i
            else:
                rtnK = getK(dic[r], i)
                # print(f"rtnK={rtnK}")
                if rtnK == -1: return []
                res[rtnK] = r
                zeros.remove(rtnK)
                dic[r] = i
    return res

def avoidFlood(rains):
    def getK(l, r):

        if len(zeros) < 1:
            return -1

        start, end = 0, len(zeros)-1

        while start <= end:
            mid = (start+end)//2

            print(f"start={start}, end={end}, mid={mid}, zeros={zeros}")
            if l < zeros[mid] < r:
                return zeros[mid]
            elif zeros[mid] > r:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    res = []
    zeros = []
    dic = {}
    for i, r in enumerate(rains):
        if r == 0:
            res.append(1)
            zeros.append(i)
        elif r > 0:
            res.append(-1)
            if r not in dic:
                dic[r] = i
            else:
                rtnK = getK(dic[r], i)
                if rtnK == -1: return []
                res[rtnK] = r
                zeros.remove(rtnK)
                dic[r] = i
    return res

def avoidFlood2(rains: List[int]) -> List[int]:
    res = []
    zeros = set()
    dic = {}
    for i, r in enumerate(rains):
        if r == 0:
            res.append(1)
            zeros.add(i)
        elif r > 0:
            res.append(-1)
            if r not in dic:
                dic[r] = i
            else:
                findK = -1
                for k in zeros:
                    if dic[r] < k < i:
                        findK = k
                        break
                if findK == -1: return []
                res[k] = r
                zeros.remove(k)
                dic[r] = i
    return res
rains = [1,2,3,0,0,3,0,2]
# rains=[1,2,0,1,2]
print(avoidFlood(rains))
