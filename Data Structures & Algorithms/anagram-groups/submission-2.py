class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            pattern = [0] * 26
            for char in word:
                pattern[ord(char) - ord('a')] += 1
            pattern_key = tuple(pattern)
            if pattern_key not in groups:
                groups[pattern_key] = []
            groups[pattern_key].append(word)
        return list(groups.values())