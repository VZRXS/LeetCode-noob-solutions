#!/usr/bin/env python


class Solution(object):
    # 9. Palindrome Number
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            xx = str(x)
            for i in range(0, len(xx) // 2):
                low_digit = xx[i]
                high_digit = xx[-1 - i]
                if low_digit != high_digit:
                    return False
            if int(xx) <= 2**31 - 1 and int(xx) >= -2**31:
                return True


if __name__ == '__main__':
    print(Solution().isPalindrome(x=123321))
