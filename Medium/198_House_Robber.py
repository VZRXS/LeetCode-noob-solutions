#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 198. House Robber
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [nums[0], nums[1]]

        if len(nums) >= 3:
            dp.append(dp[0] + nums[2])

        for i in range(len(dp), len(nums)):
            dp.append(max(dp[i - 3:i - 1]) + nums[i])
        return max(dp)


if __name__ == '__main__':
    print(Solution().rob(nums=[[2, 7, 9, 3, 1]]))
