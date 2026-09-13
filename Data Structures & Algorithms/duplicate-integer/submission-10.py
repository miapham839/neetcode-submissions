class Solution:
    '''
    - I: int arr
    - O: t/f: has duplicate?
    - E:
        - Empty input list -> return f
    - Plan:
        Init Hashset - store elements I've seen
        Iterate over input list
        For each element, if not in hashset
            add to hashset
        else:
            return false
        return true

    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == 0:
        #     return False
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

        