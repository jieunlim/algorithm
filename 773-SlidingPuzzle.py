# 773. Sliding Puzzle

import collections
class Solution(object):
    def slidingPuzzle(self, board):
        s = ''.join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index('0')))
        steps, height, width = 0, len(board), len(board[0])
        print(f"s={s}, dq={dq}, seen={seen}, steps={steps}, height={height}, width={width}")

        while dq:
            print(f"dq={dq}")
            for _ in range(len(dq)):
                t, i = dq.popleft()
                print(f"  t={t}, i={i}")
                if t == '123450':
                    print(f"t={t} return steps {steps}")
                    return steps

                x, y = i // width, i % width
                print(f"x={x}, y={y}")
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    print(f"r={r}, c={c}")
                    if height > r >= 0 <= c < width:
                        print(f"height {height} > r{r} >= 0 <= c{c} < width{width}")
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = ch[r * width + c], '0'  # swap '0' and its neighbor.
                        print(f"ch={ch}, ch[i]={ch[i]}, ch[r * width + c]={ch[r * width + c]}")
                        s = ''.join(ch)
                        print(f"s={s}")
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
                            print(f"seen={seen}, dq={dq}")
            steps += 1
            print(f"steps={steps}")
            print("")
        return -1

    def slidingPuzzle2(self, board):

        print(f"board={board}")
        moves, used, cnt = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5}, 5: {2, 4}}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]
        print(f"moves={moves}, used={used}, cnt={cnt}")
        print(f"s={s}, q={q}")

        while q:
            new = []
            for s, i in q:
                print(f"[for] q={q}")
                used.add(s)
                print(f"s={s}, i={i}, used={used}")
                if s == "123450":
                    print(f"return {cnt}")
                    return cnt

                arr = [c for c in s]
                print(f"arr={arr}")
                for move in moves[i]:
                    new_arr = arr[:]
                    print(f" move={move}, new_arr={new_arr}")
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
                    print(f"  new_arr={new_arr}, new_s={new_s}, used={used}, new={new}")
            cnt += 1
            q = new
            print(f"*cnt={cnt}, q={q}, new={new}, used={used}")
        return -1

board = [[1,2,3],[4,0,5]] #1
# board = [[1,2,3],[5,4,0]] #-1
# board = [[3,2,4],[1,5,0]] #14
# board = [[4,1,2],[5,0,3]] #5
obj = Solution()
print(obj.slidingPuzzle(board))

