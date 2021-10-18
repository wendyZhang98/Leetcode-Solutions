### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0123.Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III/README.md


### Description:
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）


### Example:
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3

# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票

# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。

# 输入：prices = [1]
# 输出：0

### Solution:
# 设 f1 表示当天结束后持有股票的最大利润
# f2 表示当前结束后没有持有股票的最大利润



# 动态规划法。
# 设 f1 表示第 1 次买入股票后的最大利润，
# f2 表示第 1 次卖出股票后的最大利润，
# f3 表示第 2 次买入股票后的最大利润，
# f4 表示第 2 次卖出股票后的最大利润。

# 遍历过程中，直接使用 f1, f2, f3, f4 计算，
# 考虑的是在同一天买入和卖出时，收益是0，不会对答案产生影响
# 最后返回 f2 即可。


class Solution1:
    def maxProfit(self, prices):
        f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
        for price in prices[1:]:
            f1 = max(f1, -price)
            f2 = max(f2, f1+price)
            f3 = max(f3, f2-price)
            f4 = max(f4, f3+price)
        return f4

### Leetcode
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-wrnt/
class Solution2:
    def maxProfit(self, prices):
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1+prices[i])
            buy2 = max(buy2, sell1-prices[i])
            sell2 = max(sell2, buy2+prices[i])
        return sell2


print(Solution1().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(Solution2().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
