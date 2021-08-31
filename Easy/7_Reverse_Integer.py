#!/usr/bin/env python


class Solution(object):
    # 7. Reverse Integer
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xx = ''
        if x == 0:
            sign = 1
        else:
            sign = x / abs(x)
        x = abs(x)
        length = len(str(x))
        for i in range(0, length):
            xx += str(x % (10**(i + 1)) // 10**(i))

        xx = int(int(xx) * sign)
        if xx <= 2**31 - 1 and xx >= -2**31:
            return xx
        else:
            return 0

    def reverse_attempt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x).startswith('-'):
            xx = int(str(x)[:0:-1])
        else:
            xx = int(str(x)[::-1])

        if xx <= 2**31 - 1 and xx >= -2**31:
            return xx
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(x=901000))
    print(Solution().reverse_attempt2(x=-901000))
