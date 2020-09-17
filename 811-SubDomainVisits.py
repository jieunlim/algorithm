# 811. Subdomain Visit Count
# the address like a.b.c, we will count a.b.c, b.c, and c.
# To count these strings, we will use a hash map.
# To split the strings into the required pieces, we will use library split functions
# time O(n), n is the length of cpdomains
# space O(n)

def subdomainVisits(cpdomains):
    from collections import defaultdict

    dict = defaultdict(int)

    for i in range(len(cpdomains)):
        vCnt, domain = cpdomains[i].split(" ")
        domains = domain.split(".")
        print(domains)
        for i in range(len(domains)):
            key = ".".join(domains[i:])
            dict[key] += int(vCnt)
    # print(f"dict = {dict}")

    res = []
    for d, i in dict.items():
        print(d, i)
        # res.append(str(i) + " " + d)
        res.append(" ".join(str(i), d))
    return res

    # https://leetcode.com/problems/subdomain-visit-count/discuss/121770/Python-short-and-understandable-solution-68-ms
    # import collections
    # counter = collections.Counter()
    # for cpdomain in cpdomains:
    #     print(f"cpdomain={cpdomain}")
    #     count, *domains = cpdomain.replace(" ", ".").split(".")
    #     print(f"count={count}, {domains} ")
    #     for i in range(len(domains)):
    #         counter[".".join(domains[i:])] += int(count)
    # return [" ".join((str(v), k)) for k, v in counter.items()]

s = ["9001 discuss.leetcode.com"]
s = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(s))


# next challenges
# 138. Copy List with Random Pointer
# 219. Contains Duplicate II
# 1166. Design File System