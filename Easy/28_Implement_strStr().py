#!/usr/bin/env python3


class Solution(object):
    # 28. Implement strStr()
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i] != needle[j]:
                    break
        if i <= len(haystack) - len(needle) and j == len(needle) - 1:
            return i
        else:
            return -1

    def strStr_attempt2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle):] == needle:
                return i
        else:
            return -1


if __name__ == '__main__':
    print(Solution().strStr(haystack="", needle=""))
    print(Solution().strStr_attempt2(haystack="abb", needle="bbb"))
