class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        U:
            I: array of integers
            O: boolean
                - True if any value appears more than once
                - False if all values are unique
            C: array of only int
            E: 
            - Empty array -> return False
            - Invalid character in array -> 
        Plan:
            - Initiate empty set
            - Iterate over the array
            - If val in set:
                return true
            - Else
                add val to set
            return false
        '''
        val_set = set()
        for i in nums:
            if i in val_set:
                return True
            else:
                val_set.add(i)
        return False