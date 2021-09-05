#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


if __name__ == '__main__':
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
