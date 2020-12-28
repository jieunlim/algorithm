# 408. Valid Word Abbreviation

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i, j, num = 0, 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]: return False

                i += 1
                j += 1
            else:
                num = int(abbr[j])
                if num == 0: return False
                while j + 1 < len(abbr) and abbr[j + 1].isnumeric():
                    num = num * 10 + int(abbr[j + 1])
                    j += 1
                i += num
                j += 1

            # print(f"i={i},, j={j}, num={num}")
        return i == len(word) and j == len(abbr)

# "internationalization"
# "i5a11o1"