class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda i:i[1])
        res = []
        res.append(intervals[0])

        remove = 0

        for start, end in intervals[1:]:
            lastend = res[-1][1]
            if start < lastend:
                remove += 1
            else:
                res.append([start, end])
        return remove
            


        