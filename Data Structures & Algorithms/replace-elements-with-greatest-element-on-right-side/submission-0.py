class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Ans array
        ans = [0] * len(arr)
        # Current max
        curMax = 0
        # Traverse right to left
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                curMax = arr[i]
                ans[i] = -1
                continue
            ans[i] = curMax
            curMax = max(curMax, arr[i])
        return ans

