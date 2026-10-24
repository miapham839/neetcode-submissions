class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        if not intervals:
            return []
        # Sort by 1st element
        intervals.sort(key= lambda x : x[0])

        # Merged list
        merged = []
        # Loop
        prevStart = -1
        prevEnd = -1
        count = 0
        for i, (start, end) in enumerate(intervals):
            if prevStart <= start <= prevEnd:
                merged[count - 1] = [prevStart, prevEnd if prevEnd >= end else end]
                prevEnd = prevEnd if prevEnd >= end else end
            else:
                merged.append([start, end])
                count += 1
                prevStart = start
                prevEnd = end
        return merged