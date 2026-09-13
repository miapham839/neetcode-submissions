class Solution:
    '''
    - I: int array nums, int target
    - O: indices i and j that has sum of values = target. i != j
    - E

    Plan:
    - Brute force: Nested for loops
    - Aim: O(n) complexity
    ans = []
    - For i in range len(nums):
        to_find = target - num
        if to_find in hashmap.items():
            if i > hashmap[to_find]:
                ans.append(hashmap[to_find])
                ans.append(i)
            else
                ans.append(i)
                ans.append(hashmap[to_find])
        add to hashmap (val - index of current val)

    '''
    # Hashmap 1 pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        seen = {}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in seen:
                if i > seen[to_find]:
                    ans.append(seen[to_find])
                    ans.append(i)
                else:
                    ans.append(i)
                    ans.append(seen[to_find])
            seen[nums[i]] = i
        return ans

    # Brute force
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)): 
    #             if i == j:
    #                 continue
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]
    #     return []

