### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0122.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II/README.md


### Description:
# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）


### Example:
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3

# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0


### Solution:
# 设 f1 表示当天结束后持有股票的最大利润
# f2 表示当前结束后没有持有股票的最大利润

# 初始第 1 天结束时，f1 = -prices[0]，f2 = 0。

# 从第 2 天开始，当天结束时：
# 若持有股票：
# 则可能是前一天持有股票，然后继续持有；也可能是前一天没有持有股票，然后当天买入股票
# 最大利润 f1 = max(f1, f2-prices[i])

# 若没有持有股票：
# 则可能是前一天没持有股票，今天也没持有股票；或者前一天持有股票，然后今天卖出。
# 最大利润 f2 = max(f2, f1+prices[i])。
# 最后返回 f2 即可。


class Solution:
    def maxProfit(self, prices):
        f1, f2 = -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, f2-price) # 当天持有股票
            f2 = max(f2, f1+price) # 当天不持有股票
        return f2


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))