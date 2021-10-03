### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0021.Merge%20Two%20Sorted%20Lists/README.md


### Description:
# 将两个升序链表合并为一个新的升序链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。

# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]


# Definition for singly-linked list.
class Node(object):
  def __init__(self, value=None, next=None):
    self.val = value
    self.next = next

def mergeTwoLists(l1, l2):
    dummy = Node()  # dummy: new Linked_List
    cur = dummy         # cur：sliding Node
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

link_1 = Node(1, Node(3, Node(5, Node(7, Node(9, Node(11, Node(13, Node(15, Node(17)))))))))
link_2 = Node(2, Node(4, Node(6, Node(8, Node(10, Node(12, Node(14, Node(16, Node(18)))))))))
root = mergeTwoLists(link_1, link_2)
while root:
    print(root.val)
    root = root.next