
# 443. String Compression
# https://leetcode.com/problems/string-compression/discuss/92568/Python-Two-Pointers-O(n)-time-O(1)-space

def compress( chars):
    left = i = 0
    while i < len(chars):
        char, length = chars[i], 1
        print(f"i={i}, char={char}, length={length}")
        while (i + 1) < len(chars) and char == chars[i + 1]:
            length, i = length + 1, i + 1
            print(f"   length={length}, i={i}")
        chars[left] = char
        print(f"  chars={chars}, left={left}")

        if length > 1:
            len_str = str(length)
            chars[left + 1:left + 1 + len(len_str)] = len_str
            left += len(len_str)
        print(f"len_str={len_str}, char={char}, left={left}, {chars[left + 1:left + 1 + len(len_str)]}")
        left, i = left + 1, i + 1
        print(f"left={left}, i={i}")

    return left

# https://leetcode.com/problems/string-compression/discuss/122241/Python-solution-with-detailed-explanation
# Maintain a rptr and wptr to write in-place.
# Use 2 while loops - outer loop rptr < len(chars) and inner loops counts the streak of common characters.
# Always write the character, but only write the frequency when it is more than 1. Note that when f = 12, we need to write two characters: "1" and "2".

def compress2( chars):

    rptr, wptr = 0, 0
    while rptr < len(chars):
        ch, f = chars[rptr], 0
        print(f"ch={ch}, f={f}")
        while rptr < len(chars) and chars[rptr] == ch:
            rptr, f = rptr+1, f+1
            print(f"rptr={rptr}, f={f}, wptr={wptr}")
        chars[wptr], wptr = ch, wptr + 1
        print(f"chars={chars}, wptr={wptr}, f={f}")
        if f > 1:
            for c in str(f):
                print(f" for : c={c}, chars[wptr]={chars[wptr]}, wptr={wptr}")
                chars[wptr], wptr = c, wptr + 1
                print(f" for - c={c}, chars[wptr]={chars[wptr]}, wptr={wptr}")
        print(f"chars={chars}")
    return wptr

chars=["a","a","b","b","b","b","b","b","b","b","b","b","b","c","c"]
print(compress2(chars))