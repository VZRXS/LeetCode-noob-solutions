#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointers
        slow = 0
        for num in nums:
            if num != val:
                nums[slow] = num
                slow += 1
        return slow


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    slow = Solution().removeElement(nums=nums, val=val)
    print(nums[:slow:])