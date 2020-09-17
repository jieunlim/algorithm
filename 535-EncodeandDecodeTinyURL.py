# 535. Encode and Decode TinyURL

# 1.using simple counter
# - limited by the reange of int
# -If excessively large number of URLs have to be encoded, after the range of
# int is exceeded, integer overflow could lead to overwriting the previous URLs' encodings,
# leading to the performance degradation
# -The length of the URL isn't necessarily shorter than the incoming
# longURL. It is only dependent on the relative order in which the URLs are encoded.
# -One problem with this method is that it is very easy to predict the next code generated,
# since the pattern can be detected by generating a few encoded URLs.

# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
# approach 5 - random fixed-length encoding
import string, random
class Codec:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        print(f"self.code2url={self.code2url}")
        print(f"self.url2code={self.url2code}")
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]

longUrl = "https://leetcode.com/problems/design-tinyurl"
obj = Codec()
shortUrl = obj.encode(longUrl)
print(obj.alphabet)
print(f"shortUrl = {shortUrl}")
print(f"longUrl= {obj.decode(shortUrl)}")

x = 10
print(type(x))

x = 10000000000000000000000000000000000000000000
print(type(x))


# Printing 100 raise to power 100
print(type(100**100))