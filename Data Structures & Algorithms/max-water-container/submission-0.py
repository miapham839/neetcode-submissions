class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            if cur > max_area:
                max_area = cur
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return max_area
        