class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute force:
        - For each num in nums
            - Create a copy of the list
            - Turn its corresponding index in list into 1
            - Loop through the list and compute product, append to result list
            - O(n^2) time, O(n^2) space

        Better:
        - Init result list
        - For each index in nums:
            loop:
            if index --> skip
            compute product incrementally
        Still O(n^2) time, but o(n) space

        How to reduce to O(n), with division
        - Compute product of every num in nums, the divide by input list
        - Edge case, if there's a num = 0 in the orig list, the product will become 0
        --> fix: Skip zeros when computing product, return list full of zeros except the index where the 0 is --> fill with the 0 excluded product
            - But what if there are multiple zeros?? Then product at those 0 indices will also be zero ---> Can't skip zero when computing products directly
            - Count first: If there are multiple 0s, return all 0s
        There must be a more elegant way...
    Input: nums = [-1,0,1,0,3]
    Output: [0,0,0,0,0]

        """
        res = [0] * len(nums)
        zero_count = 0
        zero_index = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * len(nums)
                zero_index = i
        product = 1
        for num in nums:
            if num == 0:
                continue
            product *= num
        if zero_count > 0:
            res[zero_index] = product
        else:
            res = [product // num for num in nums]
        return res
