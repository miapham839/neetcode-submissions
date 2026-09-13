class Solution:
    '''
    - I: int array nums 
    - O: int arr that is concatenation of two nums arrays.
    - Edge cases:
        - empty ans arr?

    Plan:
    init ans arr
    loop over nums -> for each num in num, insert into positions i and i + n in ans
    '''
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums)*2)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans

        