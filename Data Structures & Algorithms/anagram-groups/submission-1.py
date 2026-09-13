class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i, word in enumerate(strs):
            pattern = []
            for char in word:
                pattern.append(char)
            pattern_key = ''.join(sorted(pattern))
            if pattern_key not in groups:
                groups[pattern_key] = []
            groups[pattern_key].append(word)
        return list(groups.values())