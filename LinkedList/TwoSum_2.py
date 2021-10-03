### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0400-0499/0445.Add%20Two%20Numbers%20II/README.md


### Description
# 给你两个非空链表来代表两个非负整数
# 数字最高位位于链表开始位置
# 它们的每个节点只存储一位数字
# 将这两数相加会返回一个新的链表

# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    carry, dummy = 0, ListNode(-1)
    while s1 or s2 or carry:
        carry += (0 if not s1 else s1.pop()) + (0 if not s2 else s2.pop())  # list.pop(): get the last element
        node = ListNode(carry % 10)
        node.next = dummy.next
        dummy.next = node
        carry //= 10
    return dummy.next


# 7123
# 982
# 8105
link_1 = ListNode(7, ListNode(1, ListNode(2, ListNode(3))))
link_2 = ListNode(9, ListNode(8, ListNode(2)))

root = addTwoNumbers(link_1, link_2)
while root:
    print(root.val)
    root = root.next