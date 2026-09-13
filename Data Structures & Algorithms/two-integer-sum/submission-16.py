class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - the minus solution
        - what about set/ has map usage?? --> Try to code this
        """
        # indx_dict = {} 
        # for i in range(len(nums)):
        #     if ((target - nums[i]) in indx_dict.keys()):
        #         return [indx_dict[target - nums[i]], i]
        #     indx_dict[nums[i]] = i

        # Brute force approach
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
        # To do: Write brute force, write sorting, compare and review everything to review code style. Take notes