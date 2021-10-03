### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0155.Min%20Stack/README.md


### Description:
# 设计一个支持 push，pop，top操作，并能在常数时间内检索到最小元素的栈
# push(x) —— 将元素 x 推入栈中
# pop() —— 删除栈顶的元素
# top() —— 获取栈顶元素
# getMin() —— 检索栈中的最小元素


# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mins = [float('inf')]

    def push(self, val):
        self.s.append(val)
        self.mins.append(min(self.mins[-1], val))

    def pop(self):
        self.s.pop()
        self.mins.pop()

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

