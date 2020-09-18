
# 301. Remove Invalid Parentheses

# https://www.youtube.com/watch?v=kAIklThnh-Q

# https://youtu.be/kAIklThnh-Q
from typing import List
import collections
class Solution2:
    def removeInvalidParentheses2(self, s):

        def isValid(candidate):
            count = 0
            for i, p in enumerate(candidate):
                if p == '(': count += 1
                if p == ')': count -= 1
                if count < 0:
                    return False
            return count == 0

        def getCandidates(candidiate):

            res = set()
            for i in range(len(candidate)):
                if candidate[i] not in '()': continue
                res.add(candidate[:i] + candidate[i+1:])
            return res

        results = set()
        candidates = set([s])

        while not results:
            newCandidates = set()
            for i, candidate in enumerate(candidates):
                if isValid(candidate):
                    results.add(candidate)
                elif not results:
                    newCandidates |= getCandidates(candidate)

            candidates = newCandidates
        return list(results)

    def removeInvalidParentheses(self, s):
        def valid(candidate):
            count = 0
            print(f"  [valid] ")
            for ch in candidate:
                if ch == '(': count += 1
                if ch == ')': count -= 1

                if count < 0: return False
            return count == 0

        def get_next(candidate):
            print(f"  [get_next] candidate={candidate}")
            r = set()
            for i, ch in enumerate(candidate):
                if ch not in '()': continue
                r.add(candidate[:i] + candidate[i+1:])
                return r
                # yield candidate[:i] + candidate[i+1:]

        results = set()
        candidates = set([s])
        print(f"results={results}, candidates={candidates}")
        while not results:
            next_candidates = set()
            print(f"candidates={candidates}")
            for candidate in candidates:
                print(f"  candidate={candidate}")
                if valid(candidate):
                    results.add(candidate)
                    print(f"  YES-valid, results = {results}")
                elif not results:
                    # next_candidates.update(get_next(candidate))
                    rtnCandidate = get_next(candidate)
                    next_candidates |= rtnCandidate
                    print(f"  next_candidates={next_candidates}")
            candidates = next_candidates
        return list(results)

s = "()())()"
# s=")("
# s = "(()"
obj = Solution2()
print(obj.removeInvalidParentheses(s))

class Solution3:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(candidate):
            count = 0
            for ch in candidate:
                if ch == '(': count += 1
                if ch == ')': count -= 1
                if count < 0: return False
            return count == 0

        def get_min_removals():
            l = r = 0
            for ch in s:
                if ch == '(': l += 1
                if ch == ')':
                    if l:
                        l -= 1
                    else:
                        r += 1
            return l, r

        def get_next(candidate, loc, last_rm, l, r):
            for i, ch in enumerate(candidate[loc:], loc):
                if ch not in '()': continue
                if i and candidate[i - 1] == ch: continue
                if last_rm == '(' and ch == ')': continue
                if not l and ch == '(': continue
                if not r and ch == ')': continue
                yield candidate[:i] + candidate[i + 1:], i, ch, l - int(ch == '('), r - int(ch == ')')

        l, r = get_min_removals()

        results = []
        candidates = collections.deque([(s, 0, '', l, r)])
        while candidates:
            # candidate = candidates.popleft() # BFS
            candidate = candidates.pop()  # DFS
            if sum(candidate[-2:]) == 0 and valid(candidate[0]):
                results.append(candidate[0])
            else:
                candidates.extend(get_next(*candidate))
        return results



'''
results=set(), candidates={'()())()'}
candidates={'()())()'}
  candidate=()())()
  [valid] 
  [get_next] candidate=()())()
  next_candidates={'()()()', '()()))', ')())()', '()))()', '(())()', '()())('}
candidates={'()()()', '()()))', ')())()', '()))()', '(())()', '()())('}
  candidate=()()()
  [valid] 
  YES-valid, results = {'()()()'}
  candidate=()()))
  [valid] 
  candidate=)())()
  [valid] 
  candidate=()))()
  [valid] 
  candidate=(())()
  [valid] 
  YES-valid, results = {'()()()', '(())()'}
  candidate=()())(
  [valid] 
['()()()', '(())()']

'''
'''
results=set(), candidates={'()())()'}
candidates={'()())()'}
  candidate=()())()
  [valid] 
  [get_next] candidate=()())()
  next_candidates={'()))()', '(())()', '()()()', '()()))', '()())(', ')())()'}
candidates={'()))()', '(())()', '()()()', '()()))', '()())(', ')())()'}
  candidate=()))()
  [valid] 
  [get_next] candidate=()))()
  next_candidates={')))()', '()))(', '())()', '())))'}
  candidate=(())()
  [valid] 
  YES-valid, results = {'(())()'}
  candidate=()()()
  [valid] 
  YES-valid, results = {'()()()', '(())()'}
  candidate=()()))
  [valid] 
  candidate=()())(
  [valid] 
  candidate=)())()
  [valid] 
['()()()', '(())()']
'''

'''
results=set(), candidates={'()())()'}
candidates={'()())()'}
  candidate=()())()
  [valid] 
  [get_next] candidate=()())()
  next_candidates={'()())(', ')())()', '(())()', '()()()', '()()))', '()))()'}
candidates={'()())(', ')())()', '(())()', '()()()', '()()))', '()))()'}
  candidate=()())(
  [valid] 
  [get_next] candidate=()())(
  next_candidates={'()))(', ')())(', '()()(', '(())(', '()())'}
  candidate=)())()
  [valid] 
  [get_next] candidate=)())()
  next_candidates={')()))', ')))()', '()))(', ')()()', ')())(', '()()(', '(())(', '()())', '())()'}
  candidate=(())()
  [valid] 
  YES-valid, results = {'(())()'}
  candidate=()()()
  [valid] 
  YES-valid, results = {'(())()', '()()()'}
  candidate=()()))
  [valid] 
  candidate=()))()
  [valid] 
['(())()', '()()()']

'''



















'''
class Solution(object):
    # https://leetcode.com/problems/remove-invalid-parentheses/discuss/75079/Python-DP-Solution
    def removeInvalidParentheses(self, s):

        def minDrop(s, si, oc, cache, pseq):

            print(f"s={s}, si={si}, oc={oc}, cache={cache}, pseq={pseq}")
            N = len(s)

            if oc < 0:
                return N - si + 1

            if si == N:
                print(f"si == N")
                if oc == 0:
                    pseq[si][oc] = {''}
                    print(f"pseq[si][oc]={pseq[si][oc]}, oc={oc}")
                return oc

            if cache[si][oc] != -1:
                return cache[si][oc]

            if s[si] in '()':
                print(f"1 call minDrop")
                dc0 = 1 + minDrop(s, si + 1, oc, cache, pseq)
                pseq0 = pseq[si + 1][oc]
                print(f"after call 1 - dc0={dc0}, pseq0={pseq0}")

                if s[si] == '(':
                    print(f"2 call minDrop")
                    dc1 = minDrop(s, si + 1, oc + 1, cache, pseq)
                    pseq1 = ['(' + x for x in pseq[si + 1][oc + 1]]
                    print(f"after call 2 - dc1={dc1}, pseq1={pseq1}")
                else:
                    print(f"3 call minDrop")
                    dc1 = minDrop(s, si + 1, oc - 1, cache, pseq)
                    pseq1 = [')' + x for x in pseq[si + 1][oc - 1]]
                    print(f"after call1 3 - dc1={dc1}, pseq1={pseq1}")

                cache[si][oc] = min(dc0, dc1)
                print(f"cache={cache}, dc0={dc0}, dc1={dc1}")
                # note '=' - in case of eqaulity we keep both combination sets
                if dc0 >= dc1:
                    pseq[si][oc] = pseq[si][oc].union(pseq1)

                if dc0 <= dc1:
                    pseq[si][oc] = pseq[si][oc].union(pseq0)

            else:
                print(f"4 call minDrop")
                cache[si][oc] = minDrop(s, si + 1, oc, cache, pseq)
                print(f"after call1 4")
                pseq[si][oc] = [s[si] + x for x in pseq[si + 1][oc]]
                print(f"cache={cache}, pseq={pseq}")

            return cache[si][oc]

        N = len(s)
        cache = [[-1 for x in range(N)] for x in range(N)]
        pseq = [[set() for x in range(N + 1)] for x in range(N + 1)]

        print(f"cache={cache}")
        print(f"pseq={pseq}")
        c = minDrop(s, 0, 0, cache, pseq)
        print(f"c={c}, pseq={pseq}")
        return list(pseq[0][0])

    # https://leetcode.com/problems/remove-invalid-parentheses/discuss/75057/44ms-Python-solution
    def removeInvalidParentheses2(self, s):
        removed = 0
        results = {s}
        count = {"(": 0, ")": 0}
        print(f"results={results}")

        for i, c in enumerate(s):
            print(f"i={i}, c={c}")
            if c == ")" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()  # returns an random element
                    print(f"result={result}, results={results}, removed={removed}")
                    for j in range(i - removed + 1):
                        print(f"j={j}")
                        if result[j] == ")":
                            new_results.add(result[:j] + result[j + 1:])
                            print(f"new_results={new_results}")
                results = new_results
                removed += 1
                print(f"results={results}, removed={removed}")
            else:
                if c in count:
                    count[c] += 1
                    print(f"count={count}")

        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed
        print(f"\n\ni={i}, ll={ll}, count={count}")
        for ii in range(ll - 1, -1, -1):
            print(f"ii={ii}")
            i-=1
            c = s[i]
            print(f"i={i}, c={c} count={count}")
            if c == "(" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(ii, ll):
                        if result[j] == "(":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
                    print(f"count={count}")
        print(f"results={results}")
        return list(results)

s = "()())()"
# s="())"
# ["()()()", "(())()"]
obj = Solution()
print(obj.removeInvalidParentheses2(s))


def removeInvalidParentheses(s):

    def helper(s, iStart, jStart, open, closed):
        numOpen, numClosed = 0, 0
        print(f"s={s}, iStart={iStart}, jStart={jStart}, open={open}, closed={closed}")

        for i in range(iStart, len(s)):
            if s[i] == open: numOpen += 1
            if s[i] == closed: numClosed += 1
            print(f"  i={i}, s[i]={s[i]}, numOpen={numOpen}, numClosed={numClosed}")

            if numClosed > numOpen:
                for j in range(jStart, i+1):
                    print(f"    j = {j}")
                    if s[j] == closed and (j == jStart or s[j-1] != closed):
                        print(f"      s[j]={s[j]}, s[:j]+s[j+1:]={s[:j]+s[j+1:]}")
                        helper(s[:j]+s[j+1:], i, j, open, closed)
                return
        rStr = s[::-1]
        if open == '(':
            print(f"  rStr={rStr}, call helper")
            helper(rStr, 0, 0, ')', '(')
        else:
            res.append(rStr)
            print(f"  res={res}")

    res = []
    helper(s, 0, 0, '(', ')')
    return res


s = "()())()"
print(removeInvalidParentheses(s))



class DFSSolution:
    def remove_invalid_parentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [s]

        results = []
        self.remove(s, 0, 0, results)
        return results

    def remove(self,
               str_to_check,
               start_to_count,
               start_to_remove,
               results,
               pair=['(', ')']):
        # start_to_count: the start position where we do the +1, -1 count,
        # which is to find the position where the count is less than 0
        #
        # start_to_remove: the start position where we look for a parenthesis
        # that can be removed

        count = 0
        for count_i in range(start_to_count, len(str_to_check)):
            if str_to_check[count_i] == pair[0]:
                count += 1
            elif str_to_check[count_i] == pair[1]:
                count -= 1

            if count >= 0:
                continue

            # If it gets here, it means count < 0. Obviously.
            # That means from start_to_count to count_i (inclusive), there is an extra
            # pair[1].
            # e.g. if sub_str = ()), then we can remove the middle )
            # e.g. if sub_str = ()()), the we could remove sub_str[1], it becomes (())
            #  or we could remove sub_str[3], it becomes ()()
            # In the second example, for the last two )), we want to make sure we only
            # consider remove the first ), not the second ). In this way, we can avoid
            # duplicates in the results.
            #
            # In order to achieve this, we need this condition
            #  str_to_check[remove_i] == pair[1] and str_to_check[remove_i - 1] != str_to_check[remove_i]
            # But what if str_to_check[start_to_remove] == pair[1],
            # then remove_i - 1 is out of the range(start_to_remove, count_i + 1)
            # so we need
            # str_to_check[remove_i] == pair[1] and (start_to_remove == remove_i or str_to_check[remove_i - 1] != str_to_check[remove_i])
            for remove_i in range(start_to_remove, count_i + 1):
                if str_to_check[remove_i] == pair[1] and (start_to_remove == remove_i or str_to_check[remove_i - 1] != str_to_check[remove_i]):
                    # we remove str_to_check[remove_i]
                    new_str_to_check = str_to_check[0:remove_i] + str_to_check[remove_i + 1:]

                    # The following part are the most confusing or magic part in this algorithm!!!
                    # I'm too stupid and it took me two days to figure WTF is this?
                    #
                    # So for start_to_count value
                    # we know in str_to_check, we have scanned up to count_i, right?
                    # The next char in the str_to_check we want to look at is of index (count_i + 1) in str_to_check
                    # We have remove one char bewteen start_to_remove and count_i inclusive to get the new_str_to_check
                    # So the char we wanted to look at is of index (count_i + 1 - 1) in the new_str_to_check. (-1 because we removed one char)
                    # That's count_i. BOOM!!!
                    #
                    # Same reason for remove_i
                    # In str_to_check, we decide to remove the char of index remove_i
                    # So the next char we will look at to decide weather we want to remove is of index (remove_i + 1) in str_to_check
                    # we have remove [remove_i] char of the str_to_check to get the new_str_to_check.
                    # So the char we wanted to look at when doing remove is of index (remove_i + 1 - 1) in the new_str_to_check.
                    # That's remove_i. BOOM AGAIN!!!
                    new_start_to_count = count_i
                    new_start_to_remove = remove_i
                    self.remove(new_str_to_check,
                                new_start_to_count,
                                new_start_to_remove,
                                results,
                                pair)

            # Don't underestimate this return. It's very important
            # if inside the outer loop, it reaches the above inner loop. You have scanned the str_to_check up to count_i
            # In the above inner loop, when construct the new_str_to_check, we include the rest chars after count_i
            # and call remove with it.
            # So after the above inner loop finishes, we shouldn't allow the outer loop continue to next round because self.remove in the
            # inner loop has taken care of the rest chars after count_i
            return

        # Why the hell do we need to check the reversed str?
        # Because in the above count calculation, we only consider count < 0 case to remove stuff.
        # The default pair is ['(', ')']. So we only consider the case where there are more ')'  than '('
        # e.g "(()" can pass the above loop
        # So we need to reverse it to ")((" and call it with pair [')', '(']
        reversed_str_to_check = str_to_check[::-1]
        if pair[0] == '(':
            self.remove(reversed_str_to_check, 0, 0, results, pair=[')', '('])
        else:
            results.append(reversed_str_to_check)

def main():
    sol = DFSSolution()
    # print(sol.remove_invalid_parentheses("())())"))
    # print(sol.remove_invalid_parentheses("(()(()"))

if __name__ == '__main__':
    main()
'''