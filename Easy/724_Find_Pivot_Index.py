#!/usr/bin/env python


class Solution(object):
    # 724. Find Pivot Index
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = sum(nums) - nums[0]
        l = 0
        for i in range(len(nums)):
            if l == r:
                return i
            l += nums[i]
            r -= nums[i + 1]

        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex(nums=[-1, -1, 0, 1, 1, 0]))
