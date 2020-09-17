
# 735. Asteroid Collision
def asteroidCollision(asteroids):
    res = []
    for n in asteroids:
        print(f"n={n}, res={res}")
        while res and n < 0 < res[-1]:
            print(f"  res={res}")
            if res[-1] < -n:
                res.pop()
                continue
            elif res[-1] == -n:
                res.pop()
            break
        else:
            print(f"  #res={res}")
            res.append(n)
        print(f"  #$res={res}")
    return res


# [3, 1,-2], [2, -1]
# [1,-1], [1,-2]
# [-1,1], [-2, 1], [-1,-1]


# positive - append stack
# negative -
#    larger than (stack[-1] > 0): stack.pop()
#   not stack or stack[-1] < 0: append
#   positive stack, == abs :stack.pop()

def asteroidCollision2(asteroids):
    stack = []
    for num in asteroids:
        print(f"num={num}, stack={stack}")
        if num > 0:
            stack.append(num)
            print(f" a: stack={stack}")
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(num):
                stack.pop()
                print(f" b: stack={stack}")

            if not stack or stack[-1] < 0:
                stack.append(num)
                print(f" c: stack={stack}")
            elif stack[-1] == -num:
                stack.pop()
                print(f" d: stack={stack}")

    print(f"return stack={stack}")
    return stack

def asteroidCollision3(asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans

# asteroids=[8,-8]
asteroids=[5,10,-5]
# asteroids=[-2,-2,1,-2]
print(asteroidCollision2(asteroids))

# 605. Can Place Flowers


'''
# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:  # positive
                stack.append(asteroids[i])
            else:  # negative
                flag = True
                while stack:
                    # stack-negative
                    if stack[-1] < 0:
                        break

                    # stack-positive
                    if abs(stack[-1]) == abs(asteroids[i]):
                        flag = False
                        stack.pop()
                        break

                    if abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                    else:
                        flag = False

                if flag: stack.append(asteroids[i])

        return stack

asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))
'''