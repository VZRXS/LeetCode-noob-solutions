#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 167. Two Sum II - Input array is sorted
    # Two pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # OVERTIME
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

    def twoSum_attempt2(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:   # numbers[i]+numbers[j]==target
                return [i + 1, j + 1]


if __name__ == '__main__':
    print(Solution().twoSum_attempt2(numbers=[2, 7, 11, 15], target=9))
