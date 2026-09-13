class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - the minus solution
        - what about set/ has map usage?? --> Try to code this
        """
        indx_dict = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in indx_dict.keys()):
                return [indx_dict[target - nums[i]], i]
            indx_dict[nums[i]] = i