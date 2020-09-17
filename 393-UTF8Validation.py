
# 393. UTF-8 Validation
class Solution:
    # String Manipulation
    def validUtf8(self, data):
        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # For each integer in the data array.
        for num in data:
            # Get the binary representation. We only need the least significant 8 bits
            # for any given number.
            bin_rep = format(num, '#010b')[-8:]
            print(f"num={num}, bin_rep={bin_rep}, n_bytes={n_bytes}")

            # If this is the case then we are to start processing a new UTF-8 character.
            if n_bytes == 0:

                # Get the number of 1s in the beginning of the string.
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                print(f"n_bytes={n_bytes}")
                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Else, we are processing integers which represent bytes which are a part of
                # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # We reduce the number of bytes to process by 1 after each integer.
            n_bytes -= 1

        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0

    # Bit Manipulation
    def validUtf8_2(self, data):
        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6

        print(f"mask1={bin(mask1)}, mask2={bin(mask2)}")
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            print(f"num={num}, {bin(num)}, mask={bin(mask)}, n_bytes={n_bytes}")
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1
                    print(f"n_bytes={n_bytes}, mask={bin(mask)}")
                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                print(f"num={num}, {bin(num)}, {num & mask1}, {num & mask2}")
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0

data = [197, 130, 1]   #11000101 10000010 00000001
data=[1]
obj = Solution()
# print(obj.validUtf8(data))
print(obj.validUtf8_2(data))

# a = 8
# s = bin(a)
# s1 =format(a, '#010b')[-8:]
# print(s1)



'''
def validUtf8(data):

    i = 0
    while i < len(data):
        print(f"i={i} {bin(data[i])}")
        if data[i] & 0x80 == 0:
            i += 1
            continue
        if data[i] & 0xE0 == 0xC0:
            print(f"B")
            if i+1 >= len(data):
                return False
            if data[i+1] & 0xC0 != 0x80:
                print(f"CC")
                return False
            i += 2
            continue
        if data[i] & 0xF0 == 0xE0:
            print(f"C")
            for j in range(i+1, i+3):
                if j >= len(data): return False
                if data[j] & 0xC0 != 0x80: return False
            i += 3
            continue
        if data[i] & 0xF8 == 0xF0:
            print(f"D")
            for j in range(i+1, i+4):
                if j >= len(data): return False
                if data[j] & 0xC0 != 0x80: return False
            i += 4
            continue
        return False
    return True

data = [197, 130, 0]

print(validUtf8(data))
# print(0x80)  #1000 #128
# print(0xC0)   #1100 #192
# print(0xE0)   #1110 #224
# print(0xF0)   #1111 #240



def validUtf8(data):
    i = 0
    while i < len(data):
        print(f"i={i} {bin(data[i])}, {data[i] & 240}")
        if data[i] & 128 == 0:
            print(f"A")
            i += 1
            continue
        if data[i] & 224 == 192:
            print(f"B")
            if i+1 >= len(data):
                return False
            if data[i+1] & 192 != 128:
                print(f"CC")
                return False
            i += 2
            continue
        if data[i] & 240 == 224:
            print(f"C")
            for j in range(i+1, i+3):
                if j >= len(data): return False
                if data[j] & 192 != 128:
                    print(f"  j={j}, {data[j] & 192}")
                    return False
            i += 3
            continue
        if data[i] & 248 == 240:
            print(f"D")
            for j in range(i+1, i+4):
                if j >= len(data): return False
                if data[j] & 192 != 128: return False
            i += 4
            continue
        return False
    return True
'''