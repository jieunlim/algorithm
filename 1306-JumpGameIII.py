# 1306. Jump Game III
# DFS

def canJumpIII(arr, start):
    def jump(pos):
        print(f"pos={pos}, memo={memo}, visited={visited}")

        if pos < 0 or pos >= len(arr) or pos in visited:
            print(f"    return False")
            return False

        if arr[pos] == 0:
            return True

        if pos in memo:
            return memo[pos]

        visited.add(pos)
        if jump(pos+arr[pos]) or jump(pos-arr[pos]):
            return True
        visited.remove(pos)

        memo[pos] = False
        return memo[pos]

    memo = {}
    visited = set()
    return jump(start)


arr = [4,2,3,0,3,1,2]
start = 5
arr = [3,0,2,1,2]
start = 2
# arr = [0,3,0,6,3,3,4]
# start = 6
print(canJumpIII(arr, start))


'''
def canJumpIII(arr, start):

    def jump(pos, target):
        print(f"pos={pos}, target={target}, memo={memo}")

        if pos in target:
            return True

        if pos < 0 or pos >= len(arr) or pos in visited:
            return False

        if pos in memo:
            return memo[pos]

        visited.add(pos)
        if jump(pos+arr[pos], target) or jump(pos-arr[pos], target):
            return True
        visited.remove(pos)

        memo[pos] = False
        return memo[pos]

    target = []
    for idx, val in enumerate(arr):
        if val == 0:
            target.append(idx)

    memo = {}
    visited = set()
    return jump(start, target)

'''