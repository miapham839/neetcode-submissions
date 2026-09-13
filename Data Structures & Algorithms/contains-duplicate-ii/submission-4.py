class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # num_map = {}
        # for i in range(len(nums)):
        #     if nums[i] in num_map.keys():
        #         if abs(i - num_map[nums[i]]) <= k:
        #             return True
        #     num_map[nums[i]] = i
        # return False
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False



        