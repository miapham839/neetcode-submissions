class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Plan:
        res
        init pointers i = 1, j = 2
        while i <= len(numbers) and j <= len(numbers):
            if numbers[i] + numbers[j] != target:
                if j == 4:
                    i += 1
                    j = i + 1
                else:
                    increment j
            else:
                res = [i, j]
        '''
        res = []
        i = 0
        j = 1
        while i < len(numbers) and j < len(numbers):
            if numbers[i] + numbers[j] != target:
                if j == len(numbers) - 1:
                    i += 1
                    j = i + 1
                else:
                    j += 1
            else:
                res = [i+1, j+1]
                return res
        