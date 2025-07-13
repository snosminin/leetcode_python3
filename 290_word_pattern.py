class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        wordsMap, charsMap = {}, {}
        for c, word in zip(pattern, words):
            if (c in charsMap and charsMap[c] != word) or (word in wordsMap and wordsMap[word] != c):
                return False

            wordsMap[word] = c
            charsMap[c] = word
        return True


print(Solution().wordPattern(pattern="aaaa", s="dog cat cat dog"))
