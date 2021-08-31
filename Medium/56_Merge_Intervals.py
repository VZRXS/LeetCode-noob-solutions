#!/usr/bin/env python


class Solution(object):
    # 56. Merge Intervals
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        else:
            intervals.sort()
            l = [intervals[0][0]]
            r = [intervals[0][1]]
            j = 0
            merged = []
            for i in range(1, len(intervals)):
                if r[j] >= intervals[i][0]:
                    r[j] = max(r[j], intervals[i][1])
                if l[j] <= intervals[i][0]:
                    l[j] = min(l[j], intervals[i][0])
                if r[j] < intervals[i][0]:
                    j += 1
                    l.append(intervals[i][0])
                    r.append(intervals[i][1])

            merged = [[l[_], r[_]] for _ in range(len(l))]
            return merged


if __name__ == '__main__':
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
