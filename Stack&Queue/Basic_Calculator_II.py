### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0227.Basic%20Calculator%20II/README.md
# https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/
# https://stackoverflow.com/questions/21804437/using-ord-function-ordb0-ord0


### Description:
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值
# 整数除法仅保留整数部分

# 输入：s = "3+2*2"
# 输出：7
# 输入：s = " 3/2 "
# 输出：1
# 输入：s = " 3+5 / 2 "
# 输出：5


### Solution:
# 遍历字符串 s，并用变量 preSign 记录每个数字之前的运算符，
# 对于第一个数字，其之前的运算符视为加号。
# 每次遍历到数字末尾时，根据 preSign 来决定计算方式：
# 加号：将数字压入栈；
# 减号：将数字的相反数压入栈；
# 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。


# 由于乘除优先于加减计算，因此不妨考虑先进行所有乘除运算，
# 并将这些乘除运算后的整数值放回原表达式的相应位置，则随后整个表达式的值，就等于一系列整数加减后的值。

# 基于此，我们可以用一个栈，保存这些（进行乘除运算后的）整数的值。
# 对于加减号后的数字，将其直接压入栈中；
# 对于乘除号后的数字，可以直接与栈顶元素计算，并替换栈顶元素为计算后的结果。

# 具体来说，遍历字符串 ss，并用变量 \textit{preSign}preSign 记录每个数字之前的运算符，
# 对于第一个数字，其之前的运算符视为加号。
# 每次遍历到数字末尾时，根据 \textit{preSign}preSign 来决定计算方式：

# 加号：将数字压入栈；
# 减号：将数字的相反数压入栈；
# 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
# 代码实现中，若读到一个运算符，或者遍历到字符串末尾，即认为是遍历到了数字末尾。
# 处理完该数字后，更新 \textit{preSign}preSign 为当前遍历的字符。
# 遍历完字符串 ss 后，将栈中元素累加，即为该字符串表达式的值。


class Solution:
    def calculate(self, s):
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                preSign = s[i]
                num = 0
        return sum(stack)




