### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0933.Number%20of%20Recent%20Calls/README_EN.md


### Description:
# 写一个 RecentCounter 类来计算特定时间范围内最近的请求

# 请你实现 RecentCounter 类：
# RecentCounter() 初始化计数器，请求数为 0
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）
# 确切地说，返回在 [t-3000, t] 内发生的请求数
# 保证 每次对 ping 的调用都使用比之前更大的 t 值


# 输入：
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# 输出：
# [null, 1, 2, 3, 3]


# 解法
# 在第 1、100、3001、3002 这四个时间点分别进行了 ping 请求，
# 在 3001 秒的时候， 它前面的 3000 秒指的是区间 [1,3001]， 所以一共是有 1、100、3001 三个请求，
# t = 3002 的前 3000 秒指的是区间 [2,3002], 所以有 100、3001、3002 三次请求。
# 可以用队列实现。每次将 t 进入队尾，同时从队头开始依次移除小于 t-3000 的元素。然后返回队列的大小 q.size() 即可。


import collections


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


