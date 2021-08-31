#!/usr/bin/env python


class Solution(object):
    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        if len(nums) > 1:
            while True:
                if j >= len(nums):
                    i += 1
                    j = i + 1
                    if i >= len(nums) - 1:
                        return len(nums)
                if nums[i] == nums[j]:
                    del nums[j]
                else:
                    j += 1
        else:
            return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates(nums=[1, 1]))
