class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - declare freq dic
        - check if the 2 words; freq dic equal each   other

        - sort both
        - check if equal
        """
        if len(s) != len(t):
            return False
        char_count = [0] * 26
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1
        return char_count == [0] * 26
     