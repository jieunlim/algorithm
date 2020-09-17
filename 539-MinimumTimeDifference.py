
# 539. Minimum Time Difference
# def findMinDifference(A):
#     def convert(time):
#         return int(time[:2]) * 60 + int(time[3:])
#
#     minutes = map(convert, A)
#     minutes.sort()
#
#     return min((y - x) % (24 * 60)
#                for x, y in zip(minutes, minutes[1:] + minutes[:1]))
# # https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation
# def findMinDifference2(timePoints):
#     def minutes(p):
#         h, m = map(int, p.split(':'))
#         return 60*h + m
#     mins = sorted(map(minutes, timePoints))
#     mins.append(60*24 + mins[0])
#     return min(b - a for a, b in zip(mins, mins[1:]))

def findMinDifference3(timePoints):

    def toint(s):
        h, m = s.split(':')
        print("toint:", s, int(h) * 60 + int(m))
        return int(h) * 60 + int(m)

    arr = sorted(map(toint, timePoints))
    print(f"arr={arr}")
    mini = float('inf')
    for i in range(len(arr) - 1):
        print(f"arr[i + 1]={arr[i + 1]}, arr[i]={arr[i]}")
        mini = min(arr[i + 1] - arr[i], mini)
        print(f" mini={mini}")
        if mini == 0:
            return 0

    print(f"{24 * 60}, arr[-1] {arr[-1]}- arr[0] {arr[0]}")
    mini = min(mini, 24 * 60 - (arr[-1] - arr[0]))
    return mini
A=["23:59","00:00"]
# A=["10:00","12:00", "11:20"]
print(findMinDifference3(A))


# 383. Ransom Note
# 459. Repeated Substring Pattern
# 632. Smallest Range Covering Elements from K Lists