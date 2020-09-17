
# 38. Count and Say
#  O(NM)?

def countAndSay(n):

    def cas(st):
        count = 1
        # st += '#'
        res = ''
        for i in range(len(st)):
            if i < len(st)-1 and st[i] == st[i + 1]:
                # print(f"  {st[i]}, {st[i + 1]} ")
                count += 1
                # continue
            else:
                res += str(count) + st[i]
                count = 1
        return res

    start = '1'
    for i in range(n-1):
        # print(f"i={i}, start={start}")
        start = cas(start)
        # print(f"       start={start}")

    return start

n=4
print(countAndSay(n))


# # Copied
# def countAndSay2(n):
#
#     def cns(str_):
#         res = ''
#         str_ += '#'
#         c = 1
#         for i in range(len(str_) - 1):
#             print(f"     i={i}, str_={str_}, c={c}")
#             if str_[i] == str_[i + 1]:
#                 c += 1
#                 continue
#             else:
#                 res += str(c) + str_[i]
#                 c = 1
#
#         return res
#
#     start = '1'
#     for i in range(n - 1):
#
#         print(f"i={i}, start={start}")
#         start = cns(start)
#         print(f"       start={start}")
#     return start
