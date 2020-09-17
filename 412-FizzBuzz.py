
# 412. Fizz Buzz

# next challenges 1195. Fizz Buzz Multithreaded
def fizzBuzz(n):

    res = []
    s3 = "Fizz"
    s5 = "Buzz"
    i = 1

    while i <= n:

        n3 = i % 3
        n5 = i % 5

        if n3 == 0 and n5 == 0:
            res.append(s3+s5)
        elif n3 == 0:
            res.append(s3)
        elif n5 == 0:
            res.append(s5)
        else:
            res.append(str(i))

        i += 1
    return res

print(fizzBuzz(15))

# def fizzBuzz(n):
#         result = []
#         base3 = 3
#         base5 = 5
#         base15 = 15

#         for i in range(1, n+1):
#             if i == base15:
#                 result.append('FizzBuzz')
#                 base3 = base15 + 3
#                 base5 = base15 + 5
#                 base15 += 15
#             elif i == base3:
#                 result.append('Fizz')
#                 base3 += 3
#             elif i == base5:
#                 result.append("Buzz")
#                 base5 += 5
#             else:
#                 result.append(str(i))
#         return result
