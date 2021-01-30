class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def helper(idx, tmp):
            res.append(tmp) #1 assign tmp reference
            # res.append(tmp[:])  # 2 assign new array object
            print(f"idx={idx}, res={res}, tmp id={id(tmp)}, tmp={tmp}")
            for i in range(len(res)):
                print(f"res[{i}]={id(res[i])}")

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i - 1] == nums[i]:
                    continue
                tmp.append(nums[i])
                print(f"i={i}, idx={idx}, tmp={tmp}")
                helper(i + 1, tmp)
                tmp.pop()

        helper(0, [])
        return res

    def subsetsWithDup2(self, nums):
        def helper(start, path):
            print(f"start={start}, path={path}, {id(path)}, res={res}")
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: continue
                # path = path + [nums[i]]
                # helper(i+1, path)
                helper(i + 1, path + [nums[i]])

        res = []
        nums.sort()
        helper(0, [])
        return res


obj = Solution()
nums = [1, 2]
print(obj.subsetsWithDup(nums))
# print(obj.subsetsWithDup2(nums))


# Line 7, 8 주석을 번갈아 풀어보면서, 로그로 찍힌 tmp id값을 보면 됨.
#
# res는 [[],[1],[1,2], [2]] 이렇게 생겼잖아.
# res는 요소가 배열인 배열이므로, res의 각 요소는 array의 주소값 (reference, ref) 갖고 있지.
# 실제 값은 그 reference(ref)가 가리키는 메모리 위치에 저장되어 있고.
# 즉 res의 두번째 값은 [1]이지만, [1]은 123이라는 ref주소에 저장되어 있고,
# ref의 두번째에는 123이라는 주소값을 저장하고 있어.
# ————
# res.append(tmp)라고 여기서 tmp는 array이므로 주소값(ref)을 갖고 있고, res에는 tmp주소값이 들어가있지,
# helper 함수 내부에서 tmp를 이리 저리 바꾸지만, res는 계속 tmp주소값만 append를 하니까,
# res의 모든 요소는 다 tmp주소값을 동일하 갖고 있게 되,
# 결국 그 주소값이 보여지는 데이터는 tmp의 마지막 상태 저 경우에는 tmp의 최종 값인 [2] 가 모든 res 배열 요소로,
# res = [[2],[2],[2],[2]]를 보이겠지.
# ————
#
# 이걸 피하려면 res에 매번 다른 array객체 ref 를 넣어주어야해. 그래서 res.append(tmp[:])
# 이렇게 주면 tmp의 값을 복사한 다른 array의 ref를 res에다가 넣어주니까,
# 이때 res의 모든 요소는 다른 array 객체 ref 를 품은 array가 되는거지.
# --
# 또는 line 21 에서 helper(i + 1, tmp[:]) 로 아예 객체를 새로 만들어서 argument를 주면 helper함수에서 받는 tmp는 새로운 객체이므로
# res.append(tmp) 라고 줄 수 있음.
# ————
# 이렇게 parameter로 tmp를 전달하는 의도가, call by ref가 아닌 call by value 이므로,
# 이 경우 subsetsWithDup2 함수처럼 path+num[I] 라고 argument를 전달하면
# nums라는 파라미터는 매번 새로운 array객체가 생성이 되기 때문에 이렇게 처리하면 line 30 처럼
# res.append(path)
# 요런식으로 처리하고, 굳이 tmp.pop() 같은 처리를 할 필요가 없어.
