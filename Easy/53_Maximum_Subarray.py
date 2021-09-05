#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 53. Maximum Subarray
    # Dynamic programming
    def maxSubArray(self, nums: List[int]) -> int:
        # OVERTIME
        maxsum = nums[0]
        for i in range(len(nums)):
            sums = nums[i]
            curr_maxsum = sums
            for num in nums[i + 1::]:
                curr_maxsum = max(curr_maxsum, sums + num)
                sums += num
            maxsum = max(maxsum, curr_maxsum)
        return maxsum

    def maxSubArray_attempt2(self, nums: List[int]) -> int:

        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1], 0) + nums[i])
        return max(dp)


if __name__ == '__main__':
    print(Solution().maxSubArray_attempt2(nums=[2, 7, 9, 3, 1]))
