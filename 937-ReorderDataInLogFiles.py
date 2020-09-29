# 937. Reorder Data in Log Files

# letter-logs come before digit-logs
# letter-logs are sorted alphanumerically, by content then identifier
# digit-logs remain in the same order
# N is the tatal content of logs, time complexity is O(NlogN)
class Solution:
    def reorderLogFiles2(self, logs):
        letters =[]
        digits = []

        for log in logs:

            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x:x.split()[0])
        letters.sort(key=lambda x:x.split()[1:])
        result = letters + digits

        return result

    def reorderLogFiles(self, logs):

        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        print(f"digits={digits}, letters={letters}")
        letters.sort(key=lambda x: x.split()[0])  # when suffix is tie, sort by identifier
        print(f", letters={letters}")
        letters.sort(key=lambda x: x.split()[1:])  # sort by suffix
        print(f", letters={letters}")
        result = letters + digits  # put digit logs after letter logs
        return result


obj = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(obj.reorderLogFiles(logs))


class Solution2:
    def reorderLogFiles(self, logs):
        return sorted(logs, key=self.sort)


    def sort(self, logs):
        a, b = logs.split(' ', 1)
        print(f"logs={logs}, a={a}, b={b}")
        if b[0].isalpha():
            return (0, b, a)
        else:
            return (1, None, None)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
obj = Solution2()
print(obj.reorderLogFiles(logs))

# 58. Length of Last Word
# 159. Longest Substring with At Most Two Distinct Characters
# 770. Basic Calculator IV