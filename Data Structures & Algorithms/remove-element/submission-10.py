class Solution:
    '''
    - I: int array nums, int val
    - O: k: num elements do not contain val after the list has been removed of all val occurences in-place

    Aim: o(n) time complexity
    - Plan:
    Brute force: Create new list, Iterate over every num, if not = val -> add to new list, reassign nums to new list and return len(nums)

    '''
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n