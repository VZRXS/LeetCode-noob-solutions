#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 561. Array Partition I
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sums = 0
        for i in range(0, len(nums), 2):
            sums += min(nums[i], nums[i + 1])
        return sums


if __name__ == '__main__':
    print(Solution().arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
