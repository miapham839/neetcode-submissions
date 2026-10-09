class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        # Declare left and right pointers to run binary search
        l, r = 1, max_pile
        # Run binary search on possible ks
        res = 0
        while l <= r:
            mid = (l + r) // 2
            cur_hour = 0
            for i in piles:
                cur_hour += math.ceil(float(i) / mid)
            # If mid value is valid
            if cur_hour <= h:
                res = mid
                r = mid - 1
            elif cur_hour > h:
                l = mid + 1
        return res