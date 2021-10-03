### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0002.Add%20Two%20Numbers/README.md


### Description
# 给你两个非空的链表，表示两个非负的整数
# 它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字
# 请你将两个数相加，并以相同形式返回一个表示和的链表
# 你可以假设除了数字0之外，这两个数都不会以0开头


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = Node()
    carry, cur = 0, dummy
    while l1 or l2 or carry:
        s = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
        carry, val = divmod(s, 10)
        cur.next = Node(val)
        cur = cur.next
        l1 = None if not l1 else l1.next
        l2 = None if not l2 else l2.next
    return dummy.next


link_1 = Node(1, Node(2, Node(3)))
link_2 = Node(9, Node(10, Node(2)))

root = addTwoNumbers(link_1, link_2)
while root:
    print(root.val)
    root = root.next