
# 49. Group Anagrams
import collections
# Approach 1: Categorize by Sorted String
# time O(N*KlgK), N is the length of strs, K is the maximum length of a string in strs
# space O(NK)
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    print(f"strs={strs}, ans={ans}")

    for s in strs:
        print(f"s={s}")
        ans[tuple(sorted(s))].append(s)
        print(f"ans={ans}")

    return ans.values()

# Approach 2: Categorize by Count
# counting sort
# time O(NK), N is the length of strs, K is the maximum length of a string in strs
# space O(NK)
def groupAnagrams2(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            print(f"count={count}")
            for c in s:
                print(f"{ord(c)}, {ord('a')}, ")
                count[ord(c) - ord('a')] += 1
                print(f"c={c}, count={count}")
            ans[tuple(count)].append(s)
            print(f"ans={ans}\n")
        return ans.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams2(strs))