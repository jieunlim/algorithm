# 721. Accounts Merge

# O(M*NlogN) M is the rows of the accounts, N is column length of accounts[i]

# https://www.youtube.com/watch?v=otzKJY8YhRg
# Building Graph O(#ofemails)

#         input
#         [["John", 'A', 'B'],
#         ["John", 'D'],
#         ["John", 'A', 'C'],
#         ["Mary", "M"]]

#         output
#         [["John", "A", "C", "B"],
#         ["John", 'D']
#         ["Mary", 'M']]

#         {'A':[0, 2], 'B':[0], 'C':[2], 'D':[1], "M":[3]}


from typing import List
from collections import defaultdict
class Solution(object):
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # build adj_lists  # O(\Sigma{a_i})
        email_to_name = dict()
        adj_lists = defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                # print(f"email={email}, acc[1:]={acc[1:]}")
                adj_lists[acc[1]].add(email)
                adj_lists[email].add(acc[1])
                email_to_name[email] = acc[0]
        print(f" email_to_name={email_to_name}")
        # {'jsmith@': 'John', 'j000@': 'John', 'jbrove@': 'John', 'jny@': 'John', 'mary@': 'Mary'}
        print(f" adj_lists={adj_lists}")
        # {'jsmith@': {'jsmith@', 'jny@', 'j000@'}, 'j000@': {'jsmith@'}, 'jbrove@': {'jbrove@'}, 'jny@': {'jsmith@'}, 'mary@': {'mary@'}})

        # dfs to gather connected components  O(\Sigma{a_ilog_{a_i}})
        visited = set()
        result = []
        for email in adj_lists:
            print(f"[for start] email={email}")
            if email in visited: continue
            visited.add(email)
            stack = [email]
            emails = []
            while stack:
                email = stack.pop()
                emails.append(email)
                print(f"  while: email={email}, emails={emails}, adj_lists={adj_lists}")
                for alt_email in adj_lists[email]:
                    if alt_email in visited: continue
                    visited.add(alt_email)
                    stack.append(alt_email)
                    print(f"       for - visited={visited}, stack={stack}")
            result.append([email_to_name[email]] + sorted(emails))
            print(f" result={result}")

        return result

    def accountsMerge2(self, accounts):

        # DFS code for traversing accounts.
        def dfs(i, emails):
            # if visited[i]:
            #     print("    visited return i={i}, emails={emails}, ")
            #     return
            print(f"  [dfs] i={i}, emails={emails}, visited={visited}")
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                print(f"      j={j}, email={email}, {emails}")
                for neighbor in emailDict[email]:
                    print(f"      neighbor={neighbor}, {visited[neighbor]}")
                    if not visited[neighbor]:
                        dfs(neighbor, emails)

        visited = [False] * len(accounts)
        emailDict = defaultdict(list)
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emailDict[email].append(i)
        print(f"accounts={accounts}")
        print(f"emailDict={emailDict}")

        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            print(f"i={i}, account={account}, visited={visited}")
            if visited[i]:
                print(f"visited continue")
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
            print(f"res={res}")
        return res

# {'jsmith': [0, 2], 'j000': [0], 'jbrove ': [1], 'jny': [2], 'mary': [3]})
accounts = [["John", "jsmith@", "j000@"],
            ["John", "jbrove@"],
            ["John", "jsmith@", "jny@"],
            ["Mary", "mary@"]]

# {'johnsmith@mail.com': [0, 2],
#  'john00@mail.com': [0],
#  'johnnybravo@mail.com': [1],
#  'john_newyork@mail.com': [2],
#  'mary@mail.com': [3]})
#
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
#             ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#             ["Mary", "mary@mail.com"]]
obj = Solution()
print(obj.accountsMerge2(accounts))


'''
class UnionFind(object):
    def __init__(self, n):
        self.ids = list(range(n))
        
    def find(self, i):
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i
    
    def union(self, p, q):
        p, q = self.find(p), self.find(q)
        self.ids[p] = self.ids[q]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # email to name mapping
        email_to_name = dict()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
        
        # get email to int id mapping
        email_to_ids = {email: idx for idx, email in enumerate(email_to_name.keys())}
        n = len(email_to_ids)
        
        # union the nodes
        uf = UnionFind(n)
        for account in accounts:
            for email in account[2:]:
                uf.union(email_to_ids[account[1]], email_to_ids[email])
        
        # gather the connected components
        clusters = defaultdict(list)
        for email in email_to_name:
            clusters[uf.find(email_to_ids[email])].append(email)
        
        # construct merged accounts
        result = []
        for emails in clusters.values():
            result.append([email_to_name[emails[0]]] + sorted(emails))
            
        return result

'''