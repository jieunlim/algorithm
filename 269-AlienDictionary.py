# 269. Alien Dictionary

# Build a graph
# Topological sorting

# time complexity: O(n)
# Say the number of characters in the dictionary (including duplicates) is n.
# Building the graph takes O(n).
# Topological sort takes O(V + E). V <= n. E also can't be larger than n.
# So the overall time complexity is O(n).
# https://zhuhan0.blogspot.com/2017/06/leetcode-269-alien-dictionary.html


from collections import defaultdict

class Solution:
    def alienOrder(self, words):
        def dfs(n):
            if visited[n] == -1:
                return False
            if visited[n] == 1:
                return True
            visited[n] = -1
            for m in graph[n]:
                if not dfs(m):
                    return False
            visited[n] = 1
            res.append(n)  # res.insert(0, n)

            return True

        graph = defaultdict(list)
        # build a graph
        for i in range(len(words)-1):
            len1 = len(words[i])
            len2 = len(words[i+1])
            if len1 > len2 and words[i][:len2] == words[i+1]:
                return ""

            k = 0
            while k < min(len1, len2):
                if words[i][k] != words[i+1][k]:
                    graph[words[i][k]].append(words[i+1][k])
                    break
                k += 1
        print(f"graph={graph}, words={words}")

        # topological order
        nodes = set()
        for w in words:
            nodes |= set(w)
        print(f"nodes={nodes}")

        res = []
        visited = defaultdict(int)
        for n in nodes:
            if not dfs(n):
                return ""
        return "".join(res[::-1])

words=[
  "z",
  "x"
]
# words=[
#   "z",
#   "x",
#   "z"
# ]
words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
# words = ["a","b","ca","cc"]
# words=["abc","ab"]
words = ["z","z"]  #z
words = ["z","z", "ab"]
# words = ["abc","ab"] #''

obj = Solution()
print(obj.alienOrder(words))



class Solution2:

    def alienOrder(self, words):

        def dfs(i):
            print(f"i={i}")
            seen[i] = 0
            for nei in graph[i]:
                print(f"    nei={nei}, seen={seen}")
                if nei in seen:
                    print(f"nei={nei}, seen={seen}")
                    if seen[nei] == 0:
                        return False
                else:
                    if not dfs(nei):
                        return False

            print(f"seen={seen}, i={i}")
            seen[i] = 1
            res.appendleft(i)
            print(f"res={res}")
            return True

        # records all characters appeared in words
        nodes = set()
        for word in words:
            nodes |= set(word) # s | t means s.union(t)
            print(f"nodes={nodes}, {word}")

        print(f"words={words}")
        # construct the graph
        graph = collections.defaultdict(set)
        for i in range(len(words) - 1):
            k = 0
            while k < len(words[i]) and k < len(words[i + 1]):
                # print(f"k={k}, {words[i]}, {words[i+1]}")
                if words[i][k] != words[i + 1][k]:
                    graph[words[i][k]].add(words[i + 1][k])
                    # print(f"graph={graph}")
                    break
                else:
                    k += 1

        # topologically sort the characters
        res = collections.deque()
        seen = {}
        print(f"nodes={nodes}, graph={graph}")
        for i in nodes:
            print(f"i={i}, seen={seen}")
            if i not in seen:
                if not dfs(i):
                    return ""
        return "".join(res)



    def alienOrder2(self, words):
        map = {}
        letters = [0 for i in range(26)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                letters[key] = 0
                map[key] = set()
                print(f"{words[i][j]}, key={key}, letters={letters}, map={map}")

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            idx = 0
            print(f"word1={word1}, word2={word2}")
            for j in range(min(len(word1), len(word2))):
                print(f"    j={j}, {word1[j]}, {word2[j]}")
                if (word1[j] != word2[j]):
                    key1 = ord(word1[j]) - ord('a')
                    key2 = ord(word2[j]) - ord('a')
                    count = letters[key2]
                    print(f"    key1={key1}, key2={key2}, count={count}")
                    if (key2 not in map[key1]):
                        letters[key2] = count + 1
                        map[key1].add(key2)
                        print(f"letters={letters}, map={map}")
                    break
        dictionary = collections.deque()
        res = ''
        for i in range(26):
            if (letters[i] == 0 and i in map):
                dictionary.appendleft(i)

        while (len(dictionary) != 0):
            nextup = dictionary.pop()
            res += (chr(nextup + ord('a')))
            greaterSet = map[nextup]
            for greater in greaterSet:
                letters[greater] -= 1
                if (letters[greater] == 0):
                    dictionary.appendleft(greater)
        if (len(map) != len(res)):
            return ""
        return res

    def alienOrder3(self, words):
        degree = {key: 0 for key in set(''.join(words))}
        edges = collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    if c2 not in edges[c1]: degree[c2] += 1
                    edges[c1].add(c2)
                    break
        print(f"edges={edges}")
        queue = collections.deque(filter(lambda key: not degree[key], degree.keys()))

        result = []
        while queue:
            letter = queue.popleft()
            result.append(letter)
            for lower_letter in edges[letter]:
                degree[lower_letter] -= 1
                if not degree[lower_letter]:
                    queue.append(lower_letter)

        return ''.join(result) if len(result) == len(degree) else ''


