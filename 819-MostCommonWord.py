
# 819. Most Common Word
# time O(P)
# space O(P), P is tge size of paragraph
# https://leetcode.com/problems/most-common-word/discuss/123854/C%2B%2BJavaPython-Easy-Solution-with-Explanation
# 1. remove all puctuations & change to lowercase
# 2. words count for each word not in banned set
# 3. return most common word

def mostCommonWord(para, banned):
    from collections import Counter
    import re

    para = re.findall(r'\w+', para.lower())
    banned = set(banned)

    words = []
    for w in para:
        if w not in banned:
            words.append(w)

    myCounter = Counter(words)
    return myCounter.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))

# 385. Mini Parser
# 537. Complex Number Multiplication
# 842. Split Array into Fibonacci Sequence
