#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 14. Longest Common Prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            minlen = min([len(x) for x in strs])
        else:
            return strs[0]

        if minlen >= 1:
            for i in range(minlen):
                for j in range(1, len(strs)):
                    if strs[j - 1][i] != strs[j][i]:
                        return strs[0][:i:]
            return strs[0][:minlen:]
        else:
            return ""


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(strs=["flower", "flow", "flight"]))
