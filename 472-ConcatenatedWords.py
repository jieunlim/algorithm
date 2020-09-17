# 472. Concatenated Words

def findAllConcatenatedWordsInADict2(words):
    def isQualify(w):
        print(f"   w={w}")
        if w in word_dict:
            print(f"  *return True")
            return True
        for i in range(1, len(w)):
            print(f"  i={i}, w[:i]={w[:i]}")
            if w[:i] in word_dict and isQualify(w[i:]):
                print(f"  return True w[:i]={w[:i]}")
                return True
        print(f"   return False w={w}")
        return False

    words = sorted(words, key=lambda t: len(t))
    word_dict = set()
    print(f"words={words}")

    res = []
    for w in words:
        print(f"1- w={w}")
        if isQualify(w): res.append(w)
        word_dict.add(w)
        print(f"1- res={res}, word_dict={word_dict}")
    return res

# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# print(findAllConcatenatedWordsInADict2(words))





