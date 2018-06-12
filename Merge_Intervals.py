class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals,key=lambda x: x.start)
        merged_interval = [intervals[0]]
        for idx,interval in enumerate(intervals[1:]):
            if interval.start <= merged_interval[-1].end:
                merged_interval[-1].end = max(interval.end,merged_interval[-1].end)
            else:
                merged_interval.append(interval)
        return merged_interval