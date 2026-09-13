class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        cur_max = 0
        while r <= len(prices) - 1:
            if prices[l] > prices[r]:
                l = r
            else:
                if prices[r] - prices[l] > cur_max:
                    cur_max = prices[r] - prices[l]
            r += 1
        return cur_max

        