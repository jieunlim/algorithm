
# 336. Palindrome Pairs

import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.index= -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):

        node = self.root
        for w in words:
            node = node.children[w]
        node.index = idx

    def search(self, word):
        node = self.root

        for w in words:
            child = node.children.get(w)
            if not child:
                return False

        return child.index

class Solution:
    def isPalindrome(self, word):
        def P(i, j):
            while i < len(word) and j >= 0 and i <= j and word[i] == word[j]:
                i += 1
                j -= 1
                # print(f"    i={i}, j={j}, {word[i]}, {word[j]}")

            return i == j + 2 or i == j + 1

        return P(0, len(word)-1)

    def palindromePairs(self, pairs):

        res = []
        for i in range(len(pairs)):
            for j in range(len(pairs)):
                if i == j: continue
                print(f"i={i}, j={j}, '{pairs[i] + pairs[j]}'")
                rtn = self.isPalindrome(pairs[i] + pairs[j])
                print(f"rtn = {rtn}")
                if rtn:
                    res.append([i, j])
        return res

pairs = ["abcd","dcba","lls","s","sssll"]
pairs = ["a",""]
obj = Solution()
print(obj.palindromePairs(pairs))



class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []

class Solution:
    def palindromePairs(self, words):

        # Create the Trie and add the reverses of all the words.
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1] # We want to insert the reverse.
            current_level = trie
            for j, c in enumerate(word):
                # Check if remainder of word is a palindrome.
                if word[j:] == word[j:][::-1]:# Is the word the same as its reverse?
                    current_level.palindrome_suffixes.append(i)
                # Move down the trie.
                current_level = current_level.next[c]
            current_level.ending_word = i

        # Look up each word in the Trie and find palindrome pairs.
        solutions = []
        for i, word in enumerate(words):
            current_level = trie
            for j, c in enumerate(word):
                # Check for case 3.
                if current_level.ending_word != -1:
                    if word[j:] == word[j:][::-1]: # Is the word the same as its reverse?
                        solutions.append([i, current_level.ending_word])
                if c not in current_level.next:
                    break
                current_level = current_level.next[c]
            else: # Case 1 and 2 only come up if whole word was iterated.
                # Check for case 1.
                if current_level.ending_word != -1 and current_level.ending_word != i:
                    solutions.append([i, current_level.ending_word])
                # Check for case 2.
                for j in current_level.palindrome_suffixes:
                    solutions.append([i, j])
        return solutions
