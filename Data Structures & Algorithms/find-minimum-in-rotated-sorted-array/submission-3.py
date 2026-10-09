class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if the current considered range is already sorted, or the rotated array ends up being sorted again
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            # update min right away - why?
            '''
            because: most recent mid might not be the correct ans
            -> [3,4,5,1,2]
            for example, m at 1 -> search left: [3,4,5] --> now mid = 4 
            '''
            # TODO: a test case that proves this line is crucial
            res = min(res, nums[m]) # to make sure to keep track of the absolute min, esp in case mid = min val

            # if mid belongs to the left portion of the rotated array
            if nums[m] >= nums[l]:
                # search right
                l = m + 1
            # elif mid belongs to the right portion of the rotatated array
            elif nums[m] < nums[l]:
                # search left to see if there's any smaller values
                r = m - 1
        return res