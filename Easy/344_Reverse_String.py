#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 344. Reverse String
    # Two pointers
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
        # print(s)


if __name__ == '__main__':
    Solution().reverseString(s=["h", "e", "l", "l", "o"])  # no return
