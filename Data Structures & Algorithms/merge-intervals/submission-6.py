class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  
        # Sort by 1st element
        intervals.sort(key= lambda x : x[0])

        # Merged list
        merged = []
        # Loop
        prevStart, prevEnd, count = -1, -1, 0
        for i, (start, end) in enumerate(intervals):
            if prevStart <= start <= prevEnd:
                merged[count - 1] = [prevStart, max(end, prevEnd)]
                prevEnd = max(end, prevEnd)
            else:
                merged.append([start, end])
                count += 1
                prevStart, prevEnd = start, end
        return merged