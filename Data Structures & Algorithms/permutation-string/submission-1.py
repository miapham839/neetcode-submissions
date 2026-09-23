class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}
        for i in s1:
            chars[i] = 1 + chars.get(i, 0)
        l = 0
        r = 0
        while r < len(s2):
            while s2[r] not in chars.keys():
                # Move l until it is in keys
                l = r
                if all(x == 0 for x in chars.values()):
                    return True
                # Reset char
                chars = {}
                for i in s1:
                    chars[i] = 1 + chars.get(i, 0)
                l += 1
                r += 1
                if r >= len(s2):
                    return False
            chars[s2[r]] -= 1
            while chars[s2[r]] < 0:
                chars[s2[l]] += 1
                l += 1
            if all(x == 0 for x in chars.values()):
                return True
            r += 1
        return False

'''
Stuck: what to do with trailing prefixes
How to update the window when there's an character not in abc mid string
'''
            