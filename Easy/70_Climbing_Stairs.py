#!/usr/bin/env python3


class Solution(object):
    # 70. Climbing Stairs
    # Dynamic programming
    def climbStairs(self, n: int) -> int:
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2])
        return f[n - 1]


if __name__ == '__main__':
    print(Solution().climbStairs(n=5))
