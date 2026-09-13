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
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted