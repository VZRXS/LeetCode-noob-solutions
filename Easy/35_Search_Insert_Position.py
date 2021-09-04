#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 35. Search Insert Position
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[0]:
                return 0
            elif i >= len(nums) - 1:
                return i + 1
            elif nums[i] < target and nums[i + 1] > target:
                return i + 1


if __name__ == '__main__':
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=0))
