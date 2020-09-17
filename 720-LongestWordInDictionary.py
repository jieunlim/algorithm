# 720. Longest Word in Dictionary
from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                # print(f"w={w}")
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True
        node.word = word #bfs()

    def search(self, word):
        cur = self.root

        for w in word:
            cur = cur.children.get(w)
            if not cur:
                return False
        return cur.isWord

    def bfs(self):
        q = deque([self.root])
        res = ''
        while q:
            cur = q.popleft()
            for n in cur.children.values():
                if n.isWord:
                    q.append(n)
                    print(f"q={q}, {n.word}")
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res

    def longest_word(self):
        def helper(node, partial_res):
            res = partial_res
            print(f"partial_res={partial_res}, res={res}")
            for c, child in node.children.items():
                print(f" c={c},  {child.isWord}")
                if child.isWord:
                    print(f"   partial_res={partial_res}, res={res}")
                    pot = helper(child, partial_res + c)
                    print(f"   after, pot={pot}, res={res}, c={c}")
                    if len(pot) > len(res) or  \
                            (len(pot) == len(res) and pot < res):
                        res = pot
                        print(f"   B res={res}")
            return res

        return helper(self.root, '')

class Solution:
    def longestWord(self, words):
        T = Trie()
        for word in words:
            T.insert(word)

        return T.longest_word()
        # return T.bfs()
    # https://leetcode.com/problems/longest-word-in-dictionary/discuss/186128/O(1)-Space!-NlogN-Solution!-PythonC%2B%2B
    # this takes advantage of lexicographic ordering. i think the code is self explanatory.
    # had idea after reading wofainta's solution here:
    # https://leetcode.com/problems/longest-word-in-dictionary/discuss/175385/C++-O(N-logN)-time-O(1)-space-solution
    # def longestWord2(self, words):
    #     best = prefix = ""
    #     for w in sorted(words):
    #         if w[:len(w) - 1] == prefix[:len(w) - 1]:
    #             prefix = w
    #             best = max([best, w], key=len)
    #     return best

# words = ["w","wo","wor","worl", "world", "wort"]
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
obj = Solution()
print(obj.longestWord(words))



# Trie
# 208. Implement Trie (Prefix Tree)
