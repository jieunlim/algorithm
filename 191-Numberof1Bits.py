
# 191. Number of 1 Bits
# O(1), O(1)

def hammingWeight2(n):
    cnt = 0
    while n:
        cnt += n&1
        n = n >> 1

    return cnt

n = int('11111111111111111111111111111101', 2)
print(hammingWeight2(n))



def hamingWeight(n):
    bits = 0
    mask = 1
    for i in range(32):
        print(f"i={i}, n={n}, mask={mask}, n & mask={n & mask}")
        if n & mask != 0:
            bits += 1
            print(f"    bits={bits}")
        mask <<= 1
        print(f"mask={mask}")
    return bits

n = int('11111111111111111111111111111101', 2)
n = int('00000000000000000000000000001011',2)
n = int('00000000000000000000000010000000',2)
print(hamingWeight(n))


# 338. Counting Bits