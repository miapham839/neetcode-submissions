class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap to hold value-frequency pairs
        count = {}

        # Iterate to fill the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Create a list of groups 'freq', where freq[i] will store all numbers that appear exactly i times
        freq = [[] for i in range(len(nums) + 1)]

        # For each number and its freq in the map, add to freq[frequency]
        for n, c in count.items():
            freq[c].append(n)
        
        # Init result list
        res = []

        # Loop from the largest possible frequency down to 1
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res