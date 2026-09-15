class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums list to set for O(1) lookup
        num_set = set(nums)

        # Variable to hold Longest Consecutive Sequence
        longest = 0

        # Check if num is start of a sequence
        for num in num_set:
            if num - 1 not in num_set:
                # Get the length of the sequence
                streak = 1
                cur = num
                length = 1
                while (cur + length) in num_set:
                    streak += 1
                    length += 1
                longest = max(streak, longest)
        return longest
