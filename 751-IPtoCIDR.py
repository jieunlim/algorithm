# 751. IP to CIDR

# CIDR : IP(network address)/common prefix bits length
# Network prefix
# Host identifier

class Solution(object):
    def ipToInt(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
            print(f"ans={ans}, x={x}")
        return ans

    def intToIP(self, x):
        s = []
        for i in (24, 16, 8, 0):
            s.append(str((x >> i) % 256))
            print(f"s={s}, i={i}")
        rtn = ".".join(s)
        print(f"intToIP: rtn={rtn}")
        return rtn

    def ipToCIDR(self, ip, n):
        start = self.ipToInt(ip)
        ans = []
        print(f"start={start}, ans={ans}")
        while n:
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            ans.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
            print(f"mask={mask}, ans={ans}, start={start}, n={n}")
        return ans

ip = "255.0.0.7"
n = 10
obj = Solution()
print(obj.ipToCIDR(ip, n))