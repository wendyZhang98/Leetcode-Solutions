### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0232.Implement%20Queue%20using%20Stacks/README.md


### Description:
# 请你仅使用两个栈实现先入先出队列。
# 队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false

# 说明：
# 你只能使用标准的栈操作
# 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的
# 你所使用的语言也许不支持栈。
# 你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可

# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]

# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        self._move()
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        """
        self._move()
        return self.s2[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) + len(self.s2) == 0


    def _move(self):
        """
        Move elements from s1 to s2.
        """
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()