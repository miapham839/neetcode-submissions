class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()

        res = 0
        curr = nums[0]
        streak = 0
        i = 0

        for i in range(len(nums)):
            # SKIP DUPLICATES
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # If curr (expected next num) does not match nums[i]
            if nums[i] != curr:
                streak = 0
                curr = nums[i]

            # Increment variables to check next
            curr += 1
            streak += 1
            res = max(res, streak)
            i += 1
        return res