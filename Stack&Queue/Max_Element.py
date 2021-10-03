### Link：
# https://github.com/doocs/leetcode/blob/main/lcof/%E9%9D%A2%E8%AF%95%E9%A2%9859%20-%20II.%20%E9%98%9F%E5%88%97%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC/README.md


### Description:
# 请定义一个队列并实现函数 max_value 得到队列里的最大值
# 要求函数 max_value、push_back 和 pop_front 的均摊时间复杂度都是 O(1)
# 若队列为空，pop_front 和 max_value 需要返回 -1

# 输入:
# ["MaxQueue", "push_back", "push_back", "max_value", "pop_front", "max_value"]
# [[],[1],[2],[],[],[]]
# 输出:
# [null,null,null,2,1,2]

# 输入:
# ["MaxQueue", "pop_front", "max_value"]
# [[],[],[]]
# 输出:
# [null,-1,-1]


from collections import deque

### Method 1:
### Simple Queue
### Time Complexity:
# MaxQueue: O(N)
# PushBack: O(1)
# PopFront: O(1)
### Space Complexity: O(N)


import queue


class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()

    def max_value(self): # MaxQueue: O(N)
        return max(self.deque) if self.deque else -1

    def push_back(self, value): # PushBack: O(1)
        self.deque.append(value)

    def pop_front(self): # PopFront: O(1)
        return self.deque.popleft() if self.deque else -1


### Method 2:
### Monotone two-end queue
# 本算法基于问题的一个重要性质：当一个元素进入队列的时候，它前面所有比它小的元素就不会再对答案产生影响
# 举个例子，如果我们向队列中插入数字序列 1 1 1 1 2
# 那么在第一个数字 2 被插入后，数字 2 前面的所有数字 1 将不会对结果产生影响
# 因为按照队列的取出顺序，数字 2 只能在所有的数字 1 被取出之后才能被取出
# 因此如果数字 1 如果在队列中，那么数字 2 必然也在队列中，使得数字 1 对结果没有影响

# 按照上面的思路，我们可以设计这样的方法：
# 从队列尾部插入元素时，我们可以提前取出队列中所有比这个元素小的元素，使得队列中只保留对结果有影响的数字
# 这样的方法等价于要求维持队列单调递减，即要保证每个元素的前面都没有比它小的元素
# 那么如何高效实现一个始终递减的队列呢？
# 我们只需要在插入每一个元素 value 时，从队列尾部依次取出比当前元素 value 小的元素，直到遇到一个比当前元素大的元素 value 即可
# 上面的过程保证了只要在元素 value 被插入之前队列递减，那么在 value 被插入之后队列依然递减
# 而队列的初始状态（空队列）符合单调递减的定义
# 由数学归纳法可知队列将会始终保持单调递减
# 上面的过程需要从队列尾部取出元素，因此需要使用双端队列来实现
# 另外我们也需要一个辅助队列来记录所有被插入的值，以确定 pop_front 函数的返回值
# 保证了队列单调递减后，求最大值时只需要直接取双端队列中的第一项即可


class MaxQueue:

    def __init__(self):
        self.p = deque() # the original queue
        self.q = deque() # the monotone decreasing queue

    def max_value(self):
        return -1 if not self.q else self.q[0]

    def push_back(self, value):
        while self.q and self.q[-1] < value:
            self.q.pop()
        self.p.append(value)
        self.q.append(value)

    def pop_front(self):
        if not self.p:
            return -1
        res = self.p.popleft()
        if self.q[0] == res:
            self.q.popleft()
        return res


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()