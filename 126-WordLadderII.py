# 126. Word Ladder II

# TC O(M * N) - M is the length of words, N is the total number of words
# SC O(M * N)

# hash = {'hit':[['hit']]}
# => {'hot':[['hit', 'hot']]}
# => {'dot':[['hit', 'hot', 'dot']], 'lot':[['hit', 'hot', 'lot']]}
# => {...}
# => {'cog':[['hit', 'hot', 'dot'...'cog'], ['hit', 'hot', 'dot'...'cog']]}

# managing visited: remove from wordList or visited set()
# find candidate : O(n) 'a~z'

# https://youtu.be/vZNFOBEfib4

from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        gDict = {beginWord: [[beginWord]]}
        wordSet = set(wordList)

        while gDict:
            nDict = collections.defaultdict(list)
            for word in gDict:
                if word == endWord:
                    return gDict[word]

                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            for r in gDict[word]:
                                nDict[newWord].append(r + [newWord])

            wordSet -= set(nDict.keys())
            print(wordSet, nDict.keys())
            gDict = nDict

        return []

    # hot: [hot]
    # hit: [hot, hit]
    # dot: [hot, hit, dot]
    # lot: [hot, hit, dot, lot]

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
        return []

    wordSet = set(wordList)  # faster checks against dictionary
    layer = {}
    layer[beginWord] = [[beginWord]]  # stores current word and all possible sequences how we got to it

    while layer:
        newlayer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
        for word in layer:
            if word == endWord:
                return layer[word]  # return all found sequences
            for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        newlayer[newWord] += [j + [newWord] for j in
                                              layer[word]]  # add new word to all sequences and form new layer element
        wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops
        layer = newlayer  # move down to new layer

    return []

def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList: return []

    print(f"wordList={wordList}, begin={beginWord}, endWord={endWord}")
    wordList = set(wordList)
    layer = {}
    layer[beginWord] = [[beginWord]]
    while layer:
        newLayer = defaultdict(list)
        for w in layer:
            print(f"w={w}, layer={layer}")
            if w == endWord:
                return layer[w]
            for i in range(len(w)):
                print(f" i={i}")
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newW = w[:i] + c + w[i+1:]
                    if newW in wordList:
                        print(f"newW={newW}")
                        for j in layer[w]:
                            print(f"     j={j}, layer={layer}")
                            newLayer[newW].append(j + [newW])
                            print(f"     newLayer= {newLayer}")

        wordList -= set(newLayer.keys())  # removing the words from the word set on every iteration
        layer = newLayer
        print(f"layer={layer}")

    return []

def findLadders2(beginWord, endWord, wordList):
    if endWord not in wordList: return []

    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = defaultdict(list)
        for w in layer:
            print(f"w={w}, layer={layer}")
            if w == endWord:
                res.extend(k for k in layer[w])
                print(res)
                return layer[w]
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i] + c + w[i + 1:]
                        # print(f"i={i}, c={c}, neww={neww}")
                        if neww in wordList:
                            newlayer[neww] += [j + [neww] for j in layer[w]]
                            # newlayer[neww] += [layer[w] + [neww]]
                            print(f"neww={neww}, newlayer={newlayer}")

        wordList -= set(newlayer.keys())
        print(f"wordList={wordList}, newlayer.keys()={newlayer.keys()}, newlayer={newlayer}")
        layer = newlayer

    return res

# beginWord = "a"
# endWord = "c"
# # wordList = ["a", "b", "c"]
# wordList = ["b", "c"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# beginWord="red"
# endWord="tax"
# wordList=["ted","tex","red","tax","tad","den","rex","pee"]
# [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]


print(findLadders2(beginWord, endWord, wordList))


# Time complexity

def wordLadder(beginWrod, endWord, wordList):
    if not beginWord or not endWord or not wordList:
        return []

    layer = {}
    layer[beginWord] = [[beginWord]]
    wordList = set(wordList)
    cnt = cnt1 = cnt2 = cnt3= 0
    while layer:
        cnt += 1
        print(f"layer = {layer}, cnt={cnt}")
        newLayer = defaultdict(list)
        for w in layer:
            cnt1 += 1
            print(f"w = {w}, cnt1={cnt1}")
            if w == endWord:
                return layer[w]

            for i in range(len(w)):
                cnt2 += 1
                print(f"i = {i}, cnt2={cnt2}")
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    subW = w[:i] + c + w[i+1:]
                    if subW in wordList:
                        for w1 in layer[w]:
                            newLayer[subW].append(w1 + [subW])

        wordList -= set(newLayer.keys())
        layer = newLayer

    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# print(wordLadder(beginWord, endWord, wordList))