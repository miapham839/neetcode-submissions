class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - the minus solution
        - what about set/ has map usage?? --> Try to code this
        """
        # Hashmap one pass with minus trick
        # indx_dict = {} 
        # for i in range(len(nums)):
        #     if ((target - nums[i]) in indx_dict.keys()):
        #         return [indx_dict[target - nums[i]], i]
        #     indx_dict[nums[i]] = i

        # Brute force approach
        # for i in range (len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
            
        # Sorting + Two pointers

        # Init list to hold value-index pairs
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])
        
        # Sort the val_indx list. Whne you sort a list of sublists in Python, it compares the sublists element by element, initially by comparing the first element of each sublist
        A.sort()

        # Init pointers at start and end of nums
        i, j = 0, len(nums) - 1

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1 # why not j += 1
            else:
                j -= 1 # why not i -= 1
        return []

        ## Visualize: Why not let the two pointers have 2 ways of moving

        """
        To do: 
        [x] Write brute force
        [x] write sorting

        [] compare and review everything to review code style
        [] Take notes"""