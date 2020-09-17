class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):

        maxFrogs = curFrogs = 0
        croakCnt = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}

        for ch in croakOfFrogs:
            # print(f"ch={ch}")
            if ch == 'c':
                curFrogs += 1
                croakCnt[ch] += 1
            elif ch == 'r':
                croakCnt[ch] += 1
                if croakCnt['c'] > 0:
                    croakCnt['c'] -= 1
                else:
                    return -1
            elif ch == 'o':
                croakCnt[ch] += 1
                if croakCnt['r'] > 0:
                    croakCnt['r'] -= 1
                else:
                    return -1
            elif ch == 'a':
                croakCnt[ch] += 1
                if croakCnt['o'] > 0:
                    croakCnt['o'] -= 1
                else:
                    return -1
            elif ch == 'k':
                croakCnt[ch] += 1
                if croakCnt['a'] > 0:
                    croakCnt['a'] -= 1
                else:
                    return -1
                curFrogs -= 1

            # print(f"curFrogs={curFrogs}")
            maxFrogs = max(maxFrogs, curFrogs)

        return maxFrogs if curFrogs == 0 else -1

