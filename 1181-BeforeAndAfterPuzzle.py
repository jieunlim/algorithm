
# 1181. Before and After Puzzle
def beforeAndAfterPuzzles(phrases):
    import collections
    first = collections.defaultdict(set)
    last = collections.defaultdict(set)
    res = set()
    print(f"first={first}, last={last}, res={res}")
    for p in phrases:
        strs = p.split(' ')
        print(f"  p={p}, strs={strs}")

        if strs[0] in last:
            res |= {a + p[len(strs[0]):] for a in last[strs[0]]}
            print(f"    strs[0]={strs[0]}, last={last}, res={res}")

        if strs[-1] in first:
            res |= {p + b for b in first[strs[-1]]}
            print(f"    strs[-1]={strs[-1]}, first={first}, res={res}")

        first[strs[0]].add(p[len(strs[0]):])
        last[strs[-1]].add(p)

        print(f"  first={first}, last={last}")
    return sorted(list(res))

phrases=["writing code","code rocks"]
print(beforeAndAfterPuzzles(phrases))

# 537. Complex Number Multiplication
# 555. Split Concatenated Strings
# 696. Count Binary Substrings