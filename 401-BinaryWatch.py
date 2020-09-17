# 401. Binary Watch
class Solution(object):
    def readBinaryWatch(self, n):

        def dfs(n, hours, mins, idx):
            print(f"n={n}, hours={hours}, mins={mins}, idx={idx}")
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                print(f"return res={res}")
                return

            for i in range(idx, 10):
                print(f"i={i}")
                if i < 4:
                    print(f" i < 4, {hours | (1 << i)}, {mins}, {1 << i}")
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    print(f" i={i}, k={k}, hours={hours}, mins={mins}, {mins | (1 << k)}")
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res

    # https://leetcode.com/problems/binary-watch/discuss/88453/Python-DFS-and-complexity-analysis
    def readBinaryWatch2(self, num):
        def calc_times(idx, curr_hr, curr_min, result, n):
            print(f" idx={idx}, curr_hr={curr_hr}, curr_min={curr_min}, result={result}, n={n}")
            if n == 0:
                if curr_min < 10:
                    result.append(str(curr_hr) + ":0" + str(curr_min))
                    print(f"1. result={result}")
                else:
                    result.append(str(curr_hr) + ":" + str(curr_min))
                    print(f"2. result={result}")

            elif n > 0 and idx < len(leds):
                print(f"3")
                if 0 <= idx <= 3 and curr_hr + leds[idx] < 12:
                    print(f"4")
                    calc_times(idx + 1, curr_hr + leds[idx], curr_min, result, n - 1)
                elif idx > 3 and curr_min + leds[idx] < 60:
                    print(f"5")
                    calc_times(idx + 1, curr_hr, curr_min + leds[idx], result, n - 1)

                print(f"6")
                calc_times(idx + 1, curr_hr, curr_min, result, n)

        result = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        calc_times(0, 0, 0, result, num)
        return result



obj = Solution()
n = 1
print(obj.readBinaryWatch(n))