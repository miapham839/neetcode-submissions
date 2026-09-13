class Solution:
    '''
    - I: int array length n
    - O: majority element (appears more than n/2 times)

    Plan:
    - Iterate over each num -> Add to hashmap (freq - val)
    - Find the largest freq - get the corresponding val
    '''
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        for i in map.keys():
            if map[i] >= (len(nums)/2):
                return i

        