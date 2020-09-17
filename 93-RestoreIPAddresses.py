# 93. Restore IP Addresses

class Solution:
    def restoreIpAddresses(self, s):
        def isValid(segment):
            # if len(s) > 1 and s[0] == '0':
            #     return False
            # elif int(s) >= 0 and int(s) <= 255:
            #     return True
            # else:
            #     return False
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def dfs(idx, nth, path):
            print(f"idx={idx}, nth={nth}, path={path}, res={res}")
            # if idx >= len(s):
            #     return

            if nth == 3:
                # print(f"s={s}")
                segment = s[idx:]
                if isValid(segment):
                    res.append(path + segment)
                    print(f"res={res}")
                return

            for i in range(1, 4):
                print(f"i={i}, idx={idx}")
                if idx + i >= len(s): return
                segment = s[idx:idx + i]
                if isValid(segment):
                    dfs(idx + i, nth + 1, path + segment + ".")

        res = []
        dfs(0, 0, '')
        return res

s = "25525511135"
s='00000'
s='0100100'
obj = Solution()
print(obj.restoreIpAddresses(s))

'''
class Solution:
    def restoreIpAddresses(self, s):

        def valid(segment):
            """
            Check if the current segment is valid :
            1. less or equal to 255
            2. the first character could be '0'
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            print(f"[update_output] up segment={segment}")
            if valid(segment):
                print(f" valid!")
                segments.append(segment)
                output.append('.'.join(segments))
                print(f"  up segments={segments}, output={output}")
                segments.pop()
            print(f"up segments={segments}, output={output}")

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
            print(f"prev_pos={prev_pos}, dots={dots}")
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                print(f"curr_pos={curr_pos}")
                segment = s[prev_pos + 1:curr_pos + 1]
                print(f"segment={segment}, prev_pos={prev_pos}, curr_pos={curr_pos}")
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                        print(f"after update_output - segments={segments}")
                    else:
                        print(f"call backtrack:curr_pos={curr_pos}, dots={dots}")
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                        print(f"after backtrack - prev_pos={prev_pos}, dots={dots}, segments={segments}")
                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack()
        return output
'''
s="25525511135"
obj = Solution()
# print(obj.restoreIpAddresses(s))

class Solution2:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        print(f"s={s}, index={index}, path={path}, res={res}")
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking

        for i in range(1, 4):
            print(f"i={i}, len(s)={len(s)}")
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)

    # https://leetcode.com/problems/restore-ip-addresses/discuss/30946/DFS-in-Python
    def restoreIpAddresses2(self, s):
        res = []
        S = [([], s)]
        while S:
            l, s = S.pop()
            if len(l) == 4:
                if not s:
                    res.append('.'.join(l))
            elif len(s) <= (4 - len(l)) * 3:
                for i in range(min(3, len(s) - 3 + len(l))):
                    if i != 2 or s[:3] <= '255':
                        S.append((l + [s[:i + 1]], s[i + 1:]))
                    if s[0] == '0': break
        return res
s="25525511135"
# obj = Solution()
obj = Solution2()
# print(obj.restoreIpAddresses2(s))

