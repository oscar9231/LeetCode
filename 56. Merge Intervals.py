class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: x.start)
        res = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp.end < intervals[i].start:
                res.append(temp)
                temp = intervals[i]
            elif temp.end > intervals[i].end:
                continue
            else:
                temp.end = intervals[i].end
        res.append(temp)
        return res
