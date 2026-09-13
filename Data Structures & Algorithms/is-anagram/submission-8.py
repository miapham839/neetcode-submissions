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
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 0
            else:
                s_dict[i] += 1
        for i in t:
            if i not in t_dict:
                t_dict[i] = 0
            else:
                t_dict[i] += 1
        return s_dict == t_dict