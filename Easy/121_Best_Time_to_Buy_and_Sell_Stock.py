#!/usr/bin/env python3

from typing import List


class Solution(object):
    # 121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        # OVERTIME
        profit = 0
        for i in range(len(prices) - 1, 0, -1):
            for j in range(i, -1, -1):
                profit = max(profit, prices[i] - prices[j])
        return profit

    def maxProfit_attempt2(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]
        for i in range(1, len(prices)):
            price = min(price, prices[i - 1])
            profit = max(profit, prices[i] - price)
        return profit

    def maxProfit_attempt3(self, prices: List[int]) -> int:
        # similar to the attempt 2 but faster
        profit = 0
        minprice = prices[0]
        for price in prices[1::]:
            minprice = min(price, minprice)
            profit = max(profit, price - minprice)
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[5, 4, 3, 4, 5]))
    print(Solution().maxProfit_attempt2(prices=[5, 4, 3, 4, 5]))
    print(Solution().maxProfit_attempt3(prices=[5, 4, 3, 4, 5]))
