class Solution:
    '''
    - I: int array nums, int val
    - O: k: num elements do not contain val after the list has been removed of all val occurences in-place

    Aim: o(n) time complexity
    - Plan:
    Brute force: Create new list, Iterate over every num, if not = val -> add to new list, reassign nums to new list and return len(nums)

    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        num_val = 0

        # check bound BEFORE indexing; also handle all-vals case
        while right >= 0 and nums[right] == val:
            num_val += 1
            right -= 1
        if right < 0:
            return 0

        # include the middle element by using <=
        while left <= right:
            if nums[left] == val:
                num_val += 1
                if nums[right] != val:
                    # swap and shrink right; left will be clean after swap
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp
                    right -= 1
                else:
                    # don't double-count; just move right inward
                    right -= 1
                    continue
            else:
                left += 1

        return len(nums) - num_val