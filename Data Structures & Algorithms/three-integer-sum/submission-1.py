class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initiate result list
        res = []
        # Sort nums: O(nlogn)
        nums.sort()
        # For each num, starting from the left
        for i, num in enumerate(nums):
            # If starting number > 0, there's no way there would be triplet whose sum = 0 (sum of all positive numbers can't = 0) -> return empty list
            if i == 0 and nums[i] > 0:
                return []
            # If index > 0 and num at index = nums[index - 1]: skip
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Run 2 pointer algo to find all possible triplets that contain that num
            l, r = i + 1, len(nums) - 1
            while l < r: # why l < r? Because when l and r we've essentially checked all pairs and l > r means we're checking a pair we've already checked (understood). Why not l <= r? -> to avoid double count the middle num in input lists with odd length? what if the middle num is a part of a valid pair?? (check this)
                if nums[l] + nums[r] + num == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # What happens if we remove "and l < r" below?
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    r -= 1
        return res

