# 208. Implement Trie (Prefix Tree)

# Trie(/Try/), prefix tree
# tree data structure
# used for retrival of a key in a dataset of strings
# used for autocomplete, spelling checker, IP routing, search for a word in a dataset of strings
#
# complexity analysis
# https://leetcode.com/explore/learn/card/trie/147/basic-operations/1048/
# time complexity: If the longest of the word is N, the height of Trie will be N+1.
# The time complexitiy of all insert/search/startwith method is O(N)
# space: If we have M words to insert in total and the length of words is at most N, there will be
# at most M*N nodes in the worst case
# maximum K different characters(K is equal to 26 but might differs in different cases).
# So each node will maintain a map whose size is at most K.
# Therefore, the space complexity will be O(M*N*K)

# <comparison with hash table>:
# balanced trees & hash tables(O(1)) to store strings
# hash tables are not efficient
#  - following all keys with a common prefix
#  - enumerating a dataset of strings in lexicographical order
#  - hash key space, collision
# but time complexity is typically O(1), O(logN) in the worst time
# if there are too many collisions and we solve collisions using height-balanced BST
# time complexity to search in Trie is O(M), the hash table wins in most cases
# space - O(M*N)

import collections
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie2:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            # current.children[letter] = TrieNode()
            # current = current.children[letter]
            current = current.children[letter]
            print(f"current={id(current)}, letter={letter}, current.children[{letter}]={id(current.children[letter])}")
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True



T = Trie2()
word='apple'
T.insert(word)
print(T.search(word))
print(T.search('app'))
print(T.startsWith('app'))

#
# class Trie(object):
#
#     def __init__(self):
#         self.trie = {}
#
#     def insert(self, word):
#         trie = self.trie
#         for c in word:
#             trie = trie.setdefault(c, {})
#             print(f"trie={trie}, c={c}")
#         trie['word'] = word
#         print(f"trie={trie}")
#
#     def search(self, word):
#         trie = self.trie
#         for c in word:
#             if c not in trie:
#                 return False
#             trie = trie[c]
#         print(f"trie={trie}")
#         if trie.get('word'):
#             return True
#         return False
#
#     def startsWith(self, prefix):
#         trie = self.trie
#         for c in prefix:
#             if c not in trie:
#                 return False
#             trie = trie[c]
#         return True