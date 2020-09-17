# 127. word ladder
# TC O(M * N) - M is the length of words, N is the total number of words
# SC O(M * N)

# build dictionary : O(M*N) M is the length of words, N is the total number of words in the input word list
# search : O(M) * O(M*N) ==> O(M^2 * N)

import collections
from collections import defaultdict
class Solution(object):
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        from collections import deque
        if endWord not in wordList: return 0

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        dq = deque([(beginWord, 1)])
        wordList = set(wordList)

        while dq:
            word, cnt = dq.popleft()

            if word == endWord:
                return cnt

            wordList -= set(word)  #?? visited
            for i in range(len(word)):
                for c in alphabet:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordList:
                        dq.append((newWord, cnt + 1))

        return 0

    def ladderLength(self, beginW, endW, wList):

        wordNode = collections.defaultdict(list)

        if endW not in wList or not beginW or not endW or not wList:
            return

        L = len(beginW)
        for word in wList:
            for i in range(L):
                inW = word[:i] +'*' + word[i+1:]
                print(f"inW={inW}, word={word}")
                wordNode[inW].append(word)
        # O(M*N), M-the length of each word, N-the total number of words
        # Additionally, forming each of the intermediate word takes
        # O(M) time because of the substring operation used to create the new string
        # O(M^2 * N)
        print(wordNode)

        #BFS using Queue
        myQ = collections.deque([(beginW, 1)])
        visited = {beginW:True}

        while myQ:
            print(myQ)
            curW, level = myQ.popleft()

            print(f"curW={curW}, level={level}")
            for i in range(L):
                inW = curW[:i] +'*' + curW[i+1:]

                print(f"inW={inW}")
                for word in wordNode[inW]:
                    if word == endW:
                        print(list(visited.keys()))
                        return level+1

                    if word not in visited:
                        visited[word] = True
                        myQ.append((word, level+1))
                print(f"myQ = {myQ}")

                # wordNode[inW]=[]

        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        from collections import deque

        def getWords(word):
            # print(f"word={word}")
            res = []
            for w in wordList:
                cnt = 0
                for i in range(len(word)):
                    if w[i] != word[i]:
                        cnt += 1
                if cnt == 1:
                    res.append(w)
            return res

        dq = deque([(1, beginWord)])
        seen = set()
        while dq:
            # print(dq)
            level, word = dq.popleft()

            if word == endWord:
                return level

            # seen.add(word)
            if word in wordList: wordList.remove(word)
            candidates = getWords(word)
            # print(candidates)
            for w in candidates:
                # if w not in seen:
                dq.append((level+1, w))

        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

obj = Solution()
print(obj.ladderLength(beginWord, endWord, wordList))

'''
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
wordNode =
{'*ot': ['hot', 'dot', 'lot'], 
'h*t': ['hot'], 
'ho*': ['hot'], 
'd*t': ['dot'], 
'do*': ['dot', 'dog'], 
'd*g': ['dog'], 
'l*t': ['lot'], 
'lo*': ['lot', 'log'], 
'l*g': ['log'], 
'*og': ['dog', 'log', 'cog'], 
'c*g': ['cog'], 
'co*': ['cog']})
['hit', 'hot', 'dot', 'lot', 'dog', 'log']
'''
'''  
from collections import defaultdict
import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        print(beginWord, endWord, wordList)
        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # print(f"word={word}, i={i}")
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                # print(word[:i] + "*" + word[i+1:])
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                # print(f"all_combo_dict={all_combo_dict}")

        # {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'],
        #  'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'],
        #  'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']})

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        print(queue, visited)

        while queue:
            current_word, level = queue.popleft()
            print(f"current_word={current_word}, level={level}")
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                print(f" intermediate_word={intermediate_word}")

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    print(f"  word={word}")
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                    print(f"  visited={visited}")
                print(intermediate_word, all_combo_dict[intermediate_word])
                all_combo_dict[intermediate_word] = []
                print(intermediate_word, all_combo_dict[intermediate_word])
        return 0
'''
