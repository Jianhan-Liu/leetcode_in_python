"""
  @Author       : liujianhan
  @Date         : 2020/12/17 10:34
  @Project      : leetcode_in_python
  @FileName     : 714.买卖股票的最佳时机含手续费(M).py
  @Description  : 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
    你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
    返回获得利润的最大值。
    注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

    示例 1:
    输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
    输出: 8
    解释: 能够达到的最大利润:
    在此处买入 prices[0] = 1
    在此处卖出 prices[3] = 8
    在此处买入 prices[4] = 4
    在此处卖出 prices[5] = 9
    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    注意:

    0 < prices.length <= 50000.
    0 < prices[i] < 50000.
    0 <= fee < 50000.

    思路：
    定义状态转移方程：
    不持有：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
    对于今天不持有，可以从两个状态转移过来：1. 昨天也不持有；2. 昨天持有，今天卖出。两者取较大值。
    持有：dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    对于今天持有，可以从两个状态转移过来：1. 昨天也持有；2. 昨天不持有，今天买入。两者取较大值。

    2. 给定转移方程初始值
    对于第 0 天：
    不持有： dp[0][0] = 0
    持有（即花了 price[0] 的钱买入）： dp[0][1] = -prices[0]
"""
from typing import List


class Solution:
    # 1008ms, 23.9MB
    @staticmethod
    def max_profit(prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]

    # 772ms, 21.5MB
    @staticmethod
    def max_profit_v2(prices: List[int], fee: int) -> int:
        """转移的时候，dp[i] 只会从 dp[i−1] 转移得来，因此第一维可以去掉"""
        n = len(prices)
        dp = [0, -prices[0]]
        for i in range(1, n):
            tmp = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], tmp-prices[i])
        return dp[0]


if __name__ == '__main__':
    test_cases = [
        ([1, 3, 2, 8, 4, 9], 2)
    ]
    for tc in test_cases:
        print(Solution.max_profit(*tc))
        print(Solution.max_profit_v2(*tc))
