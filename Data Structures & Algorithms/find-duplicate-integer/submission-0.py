class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Using O(n) time and space
        '''
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
