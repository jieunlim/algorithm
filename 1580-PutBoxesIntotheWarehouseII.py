# 1580. Put Boxes Into the Warehouse II

from typing import List
import sys
def maxBoxesInWarehouse( boxes: List[int], warehouse: List[int]) -> int:
    if not warehouse: return 0
    l, r = 0, len(warehouse) - 1
    stack = []
    min_l, min_r = sys.maxsize, sys.maxsize
    print(f"min_l={min_l}, min_r={min_r}, {float('inf')}")
    while l <= r:
        min_l = min(min_l, warehouse[l])
        min_r = min(min_r, warehouse[r])
        if min_l >= min_r:
            stack.append(min_l)
            l += 1
        else:
            stack.append(min_r)
            r -= 1
        print(f"stack={stack}")

    asr = 0
    boxes.sort(reverse=True)
    print(f"stack={stack}, boxes={boxes}")
    while boxes:
        while stack and stack[-1] < boxes[-1]:
            stack.pop()
        if not stack: return asr
        stack.pop()
        boxes.pop()
        asr += 1
        print(f"stack={stack}, boxes={boxes}")
    return asr


def maxBoxesInWarehouse2( boxes: List[int], warehouse: List[int]) -> int:
    indexBox = len(boxes) - 1
    indexWarehouse = len(warehouse) - 1

    leftMin, rightMin = [0 for _ in range(indexWarehouse + 1)], [0 for _ in range(indexWarehouse + 1)]
    leftMin[0], rightMin[indexWarehouse] = warehouse[0], warehouse[indexWarehouse]
    for i in range(1, len(warehouse)):
        leftMin[i] = min(warehouse[i], leftMin[i - 1])
        rightMin[indexWarehouse - i] = min(warehouse[indexWarehouse - i], rightMin[indexWarehouse - i + 1])

    # print(f"leftMin={leftMin}, rightMin={rightMin}")
    for i in range(len(warehouse)):
        warehouse[i] = max(leftMin[i], rightMin[i])
    # print(f"warehouse={warehouse}")

    boxes.sort(reverse=True)
    warehouse.sort(reverse=True)

    print(boxes, warehouse)
    result = 0
    while indexBox >= 0 and indexWarehouse >= 0:
        # print(f"indexBox={indexBox}, indexWarehouse={indexWarehouse}, result={result}")
        while indexWarehouse >= 0 and warehouse[indexWarehouse] < boxes[indexBox]:
            indexWarehouse -= 1
            # print(f"indexWarehouse={indexWarehouse}")
        if indexWarehouse < 0: return result
        result += 1
        indexBox -= 1
        indexWarehouse -= 1
    return result


boxes = [1,2,2,3,4]
warehouse = [3,4,1,2]
boxes = [3,5,5,2]
warehouse = [2,1,3,4,5]
# boxes = [4,5,6]
# warehouse = [3,3,3,3,3]

boxes = [4,5,6,2]
warehouse = [3,2,6,3,3,7]
print(maxBoxesInWarehouse2(boxes, warehouse))


# [1,2,2,3,4]
# [3,4,1,2]
# #
# [3,5,5,2]
# [2,1,3,4,5] #3
# #
# [1,2,3]
# [1,2,3,4] #3
#
# [4,5,6]
# [3,3,3,3,3] #0