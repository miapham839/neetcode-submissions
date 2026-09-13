class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Plan:
        - dict to store seen numbers
        - iterate: if not in dict, continue, if in dict, return false
        - return true if does not find duplicates after full loop
        """
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
        