class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap to hold value-frequency pairs
        count = {}

        # Iterate to fill the hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Initialize heap
        heap = []
        for num in count.keys():
            # Push each freq-val pair to the heap
            heapq.heappush(heap, (count[num], num))
            # If heap size > k, pop the smallest
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Init list to hold top K frequents
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res