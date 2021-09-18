#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 209. Minimum Size Subarray Sum
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Two pointers
        slow = 0
        fast = 0
        sums = 0
        minlen = len(nums) + 1

        for fast in range(len(nums)):
            sums += nums[fast]
            while sums >= target:
                minlen = min(minlen, fast - slow + 1)
                sums -= nums[slow]
                slow += 1

        if minlen <= len(nums):
            return minlen
        return 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
