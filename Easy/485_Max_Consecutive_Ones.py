#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 485. Max Consecutive Ones
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Two pointers
        slow = 0
        fast = 0
        maxnum = 0
        while fast < len(nums):
            if nums[slow] != 1:
                slow += 1
            if nums[fast] != 1:
                maxnum = max(maxnum, fast - slow)
                slow = fast + 1
            fast += 1

        if nums[-1] == 1:
            maxnum = max(maxnum, fast - slow)
        return maxnum


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 1, 1, 1]))
