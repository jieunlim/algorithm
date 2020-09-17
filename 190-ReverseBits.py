
# 190. Reverse Bits
def reverseBits(n):
    revBits = 0

    for i in range(32):
        revBits <<= 1
        print(f"revBits={bin(revBits)}")
        if n & 1: revBits += 1
        n >>= 1
        print(f"n={bin(n)}, revBits={bin(revBits)}")

    return revBits

n = int('00000010100101000001111010011100', 2)
n = int('11111111111111111111111111111101', 2)
r = reverseBits(n)
print(bin(r), r)


 # 0-0
 # 1-1
 # 2-10
 # 3-11
 # 4-100
 # 5-101
 # 6-110
 # 7-111
 # 8-1000
 # 9-1001
 # 10-1010
 # 11-1011
 # 12-1100
 # 13-1101
 # 14-1110
 # 15-1111
 # 16-10000

