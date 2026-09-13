class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        ans = ""
        length = min(len(word1), len(word2))
        while i < length and j < length:
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        if len(word1) > len(word2):
            for x in range (i, len(word1)):
                ans += word1[x]
        else:
            for x in range (j, len(word2)):
                ans += word2[x]
        return ans

        