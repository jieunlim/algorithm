# 937. Reorder Data in Log Files

# letter-logs come before digit-logs
# letter-logs are sorted alphanumerically, by content then identifier
# digit-logs remain in the same order
# N is the tatal content of logs, time complexity is O(NlogN)
class Solution:
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

# 58. Length of Last Word
# 159. Longest Substring with At Most Two Distinct Characters
# 770. Basic Calculator IV