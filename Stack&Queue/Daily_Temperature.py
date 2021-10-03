### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0700-0799/0739.Daily%20Temperatures/README.md
# https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/

### Description:
# 请根据每日 气温 列表，重新生成一个列表。
# 对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
# 你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
# 提示：气温 列表长度的范围是 [1, 30000]。
# 每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。


### Solution:
# 遍历每日温度，维护一个单调栈
# 若栈为空或当日温度小于栈顶温度则直接入栈
# 反之，若当日温度大于栈顶温度，说明栈顶元素的升温日已经找到了，则将栈顶元素出栈，计算其与当日相差的天数即可
# 注意题目说的是升温的天数，而不是升温的温度
# 因此栈中应存储下标，而非温度


class Solution:
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans





