class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash set to store seen chars in the current window
        seen = set()
        longest = 0
        
        # Left pointer
        l = 0
        for r in range(len(s)):
            # If char at r is in seen, remove from the left side until there's no more occurence of the char in our window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # Add char at r
            seen.add(s[r])
            longest = max(longest, len(seen))
        return longest
            