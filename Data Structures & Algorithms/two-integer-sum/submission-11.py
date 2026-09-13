class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        U:
        - Input: array of integers
        - Output: a list of indices of elements whose sum == target
        - Constraints:
            - Indices must be unique
            - Every input has exactly one pair of indices
            - The smaller index must be first in the output list
        - Edge case:
            - empty array
        P:
        - Brute force: Nested for loop O(n^2)
        - Initiate empty list called res
        - Initiate empty dic [char:index as K-V pairs]
            Loop through list: For i in range len(list)
                if (target - nums[i]) in dic.keys():
                    append the indices to res
                else:
                    add nums[i] to the dic
        - return res
        '''
        res = []
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic.keys():
                res.append(dic[target - nums[i]])
                res.append(i)
            else:
                dic[nums[i]] = i
        return res
        