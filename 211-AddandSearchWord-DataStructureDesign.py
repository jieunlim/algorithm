# 211. Add and Search Word - Data structure design


# 1. using Hashmap
# O(M*N) M-a length of word to find, N is the number of words

# {3:{'bad','dad'}}
# 'bad'

from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.wordDict = defaultdict(set)

    def addWord(self, word):
        if word:
            self.wordDict[len(word)].add(word)

    def search(self, word):

        m = len(word)
        # O(M*N), length of word * # of words
        for dictW in self.wordDict[m]:
            i = 0
            while i < m and (dictW[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m: return True

        return False

obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
print(obj.search('bad'))
print(obj.search('.ad'))
print(obj.search('.a.'))


# 2. Using Trie
# trie root
# n          a
# u          n
# t (T)   t(T) d(T)
# s (T)
#
# search('..d')
#
# [(root, '.d')]
# [(t(n), '.d'), (t(a), '.d')]
# [(t(a), '.d') (t(u), 'd')]
# [(t(u), 'd'), (t(n), 'd')]


# https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59725/Python-easy-to-follow-solution-using-Trie.

from collections import defaultdict
class Solution:
    def __init__(self):
        self.wordDict = defaultdict(set)

    def addWord(self, word):
        self.wordDict[len(word)].add(word)

    def search(self, word):
        m = len(word)

        for w in self.wordDict[m]:
            i = 0
            while i < m and (w[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m: return True
        return False

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
class Solution2:
    def __init__(self):
        self.root = TrieNode()

    # O(M) M is the key length
    # O(M)
    def addWord(self, word):
        cur = self.root
        for w in word:
            # cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

    # O(M), O(M)
    def search(self, word):
        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            print(f"node={node.children.keys()}, w={w}")
            if not w:
                if node.isWord:
                    return True
            elif w[0] == '.':
                for n in node.children.values():
                    stack.append((n, w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n, w[1:]))
        return False

    def search2(self, word):
        def helper(node, searchWord):
            if not searchWord:
                if node.isWord:
                    self.rtn = True
                    return

            if searchWord[0] == '.':
                for n in node.children.values():
                    helper(n, searchWord[1:])
            else:
                node = node.children.get(searchWord[0])
                if not node:
                    return
                helper(node, searchWord[1:])

        cur = self.root
        self.rtn = False
        helper(cur, word)
        return self.rtn


obj = Solution2()
print(obj.addWord('runner'))
print(obj.addWord('runs'))
print(obj.addWord('add'))
print(obj.addWord('adds'))
print(obj.addWord('adder'))
print(obj.addWord('addee'))
print(obj.search3('....e.')) #T
print(obj.search('....e.')) #T



# 208. Implement Trie (Prefix Tree)
