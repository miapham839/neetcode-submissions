class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap to hold value-frequency pairs
        count = {}

        # Iterate to fill the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Build a list of (value, frequency) pairs
        freqs = list(count.items())

        # Sort ascending (by freq)
        freqs.sort(key=lambda item: item[1])

        # Initialize res list
        res = []
        # Repeatedly pop from the end of the list 
        # (to get highest freqs) k times to add to res
        for i in range(k):
            res.append(freqs.pop()[0])
        return res