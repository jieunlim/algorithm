
# 609. Find Duplicate File in System

def findDuplicate(paths):
    import collections
    groups = collections.defaultdict(list)
    for path in paths:
        directory, *files = path.split()
        print(f"directory={directory}, files={files}")
        for file in files:
            name, content = file.split('(')
            print(f" name={name}, content={content}")
            groups[content].append(directory + '/' + name)
            print(f"   groups = {groups}")
    print(f"groups.values()={groups.values()}")
    return [g for g in groups.values() if len(g) > 1]

paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(findDuplicate(paths))

# 43. Multiply Strings
# 138. Copy List with Random Pointer
# 718. Maximum Length of Repeated Subarray
