### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0092.Reverse%20Linked%20List%20II/README.md


### Description:
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right
# 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]


# Definition for singly-linked list.
class Node():
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


def reverseBetween(head, left, right):
    if head is None or head.next is None or left == right:
        return head
    dummy = Node(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next
    p, q = pre, pre.next
    cur = q
    for _ in range(right - left + 1):
        t = cur.next
        cur.next = pre
        pre, cur = cur, t
    p.next = pre
    q.next = cur
    return dummy.next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
root = reverseBetween(head=link, left=3, right=7)
while root:
    print(root.value)
    root = root.next