class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        longest = 0
        for r in range(len(s)):
            count[s[r]] += 1
            # if window size - max occurence < k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, sum(count.values()))
        return longest
        


