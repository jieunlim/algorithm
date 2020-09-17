# 68. Text Justification

# an array of words, a width maxWidth
# format the text such that each line has exactly maxWidth characters and is fully justified.
# pack your words in a greedy approach - as many words as you can in each line.
# Pad extra spaces ' ' so that each line has exactly maxWidth characters.
# Extra spaces - evenly or the empty slosts on the left will be assigned more spaces than the right
#           - for the last line, it should be left justified and no extra space between words.

# https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.

class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            print(f"w={w}, num_of_letters={num_of_letters}, len(w)={len(w)}, len(cur)={len(cur)}")
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                    print(f"i={i}, cur={cur}")
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
                print(f"res={res} ")
            cur += [w]
            num_of_letters += len(w)
            print(f"cur={cur}, num_of_letters={num_of_letters}")
        return res + [' '.join(cur).ljust(maxWidth)]

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20

obj = Solution()
print(obj.fullJustify(words, maxWidth))


# 하다 말았음...
#lecture20 Text Justification - DP
# Badness
class Solution2:
    def textJustification(self, words, maxWidth):

        def textJ(start):
            if start >= len(words):
                return MAX

            for i in range(len(words)):
                minVal = 0
                for j in range(i + 1, len(words)):
                    badVal = maxWidth - len(words[i:j]) + j - i - 1
                    minVal = min(minVal, badVal * badVal + textJ(j + 1))

            return minVal

        MAX = float('inf')
        return textJ(0)



words = ["Blah", "Blah", "Blah", "Blah", "Reallylongword"]
maxWidth = 14

# obj = Solution2()
# print(obj.textJustification(words,maxWidth))
