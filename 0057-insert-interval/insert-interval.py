class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda i:i[0])

        output = [intervals[0]]
        print(output)

        for start, end in intervals[1:]:
            lastend = output[-1][1]
            if start <= lastend:
                output[-1][1] = max(end, lastend)
            else:
                output.append([start, end])

        return output
        